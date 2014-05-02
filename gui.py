#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from interpreter import *
from player import *
from tile import *
import kivy
kivy.require('1.8.0')

"""screen configuration"""
from kivy.config import Config
Config.set('graphics', 'size', '800x600')     # screen resolution
Config.set('graphics','fullscreen', 'false')  # fullscreen mod disabled
Config.set('graphics', 'resizable', 0)        # screen cannot be resized

"""Kivy imports"""
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.atlas import Atlas
from kivy.clock import Clock


'''Main Widget'''
class Game(Widget):
    def __init__(self, *args, **kwargs):
        super(Game, self).__init__(**kwargs)
        self.player = Player()
        self.map = MapTile()
        self.update()

    def on_enter(self, *args, **kwargs): 
        """event executed if the enter key is pressed"""
        self.ids.txt_display.add_text(self.ids.txt_input.text) # adds text to text display
        self.update()                                          # updates the game and the display
        self.ids.txt_input.text = ""                           # resets text input
        Clock.schedule_once(self.refocus_txtinput)

    def update(self, *args, **kwargs):
        """updates game state and display"""
        self.update_game_state()
        self.update_display()

    def update_game_state(self, *args, **kwargs):
        """updates the game state"""
        read(self.ids.txt_display, self.player, self.ids.txt_input.text) # reads text entered by user
        self.map.update(self.player)                                     # loads informations relative to player position

    def update_display(self, *args, **kwargs):
        """updates the gui"""
        self.ids.info_box.get_player_stats(self.player)
        self.ids.info_box.display_stats()

        self.ids.minimap_box.get_player_pos(self.player)
        self.ids.minimap_box.display()

    def refocus_txtinput(self, *args, **kwargs):
        """Refocuses cursor on text input"""
        self.ids.txt_input.focus = True

    """COMMANDS"""

class BackgroundImage(BoxLayout):
    """custom BoxLayout to set a custom background image"""
    pass

class TextDisplay(Label):
    """Text Display Widget"""
    def __init__(self, *args, **kwargs):
        super(TextDisplay, self).__init__(**kwargs) 
        self.text_storage = []

    def add_text(self, text, *args, **kwargs):
        """Adds text to the console"""
        self.text_storage.append(text)              # stores the text in a list
        text_string = ""                            # resets text_string 
        if len(self.text_storage)>100:              # if list has more than 100 entries, deletes the first entry to avoid display bugs
            del self.text_storage[0]

        for i in range(0, len(self.text_storage)):  # loop to add each list entry to text_string
            log = text_string
            text_string = "".join((log, str(self.text_storage[i]),"\n"))
        self.text = text_string                     # displays text_string on the gui


class MiniMapBox(RelativeLayout):
    """Minimap Widget"""
    def __init__(self, *args, **kwargs):
        super(MiniMapBox, self).__init__(**kwargs)
        self.spritesheet = Atlas('spritesheet.atlas')  # loads spritesheet.atlas
        self.offs_x = -88                             
        self.offs_y = -76
        self.revealed_map = [(0,0)]
        self.player_pos = (0,0)
        self.display()


#    def reveal_map(self, xy, *args, **kwargs):
#        """displays coords xy of the minimap"""
#        coordinates = ((int(xy[0])*25)+self.decal_x,(int(xy[1])*25)+self.decal_y)                      # defines coordinates at which to display the map tile 
#        map_part = Image(texture=self.spritesheet["("+str(xy[0])+","+str(xy[1])+")"], pos=coordinates) # creates the widget
#        self.add_widget(map_part)                                                                      # adds widget to parent widget

    def get_player_pos(self, player, *args, **kwargs):
        """updates player position"""
        self.player_pos = player.get_pos()
        if self.player_pos not in self.revealed_map:
            self.revealed_map.append(self.player_pos)
            print(self.revealed_map)

    def draw_player_pos(self, *args, **kwargs):
        offset = ((int(self.player_pos[0])*25)-88,(int(self.player_pos[1])*25)-75)
        square = Image(texture = self.spritesheet["current_tile"], pos = offset)
        self.add_widget(square)

    def draw_tile(self, coordinates, *args, **kwargs):
        offset = ((int(coordinates[0])*25)+self.offs_x,(int(coordinates[1])*25)+self.offs_y)
        tile = Image(texture = self.spritesheet[str(coordinates)], pos = offset)
        self.add_widget(tile)

    def display(self, *args, **kwargs):
        """displays map"""
        self.clear_widgets()
        for i in range(0, len(self.revealed_map)):
            self.draw_tile(self.revealed_map[i])
        self.draw_player_pos()



class CharacterInfosBox(RelativeLayout):
    """Character Informations Box"""
    def __init__(self, *args, **kwargs):
        super(CharacterInfosBox, self).__init__(**kwargs)
        self.spritesheet = Atlas('spritesheet.atlas')  # loads spritesheet.atlas
        self.armor = False
        self.sword = False
        self.display_stats()

    def get_player_stats(self, player, *args, **kwargs):
        """collects player stats"""
        self.armor = player.has_armor()
        self.sword = player.has_sword()

    def display_stats(self, *args, **kwargs):
        """displays player stats"""
        self.clear_widgets()
        if self.armor:                                                                         # if player has armor
            platearmor = Image(texture = self.spritesheet["platearmor"], pos=(0,0))            # displays plate armor image
            self.add_widget(platearmor)
        else:
            clotharmor = Image(texture = self.spritesheet["clotharmor"], pos=(0,0))            # displays no armor image
            self.add_widget(clotharmor)
            
        if self.sword:                                                                         # displays sword image
            sword = Image(texture = self.spritesheet["sword"], pos=(-20,-6))
            self.add_widget(sword)