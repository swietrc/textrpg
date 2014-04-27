#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from interpreter import *
from player import *
import kivy
kivy.require('1.8.0')

'''Screen config'''
from kivy.config import Config
Config.set('graphics', 'size', '800x600')
Config.set('graphics','fullscreen', 'false')
Config.set('graphics', 'resizable', 0)


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
        self.update()

    def on_enter(self): 
        """event if enter key is pressed -> adds text to the console and refocuses on text input"""
#        print('User pressed enter: ', self, self.ids.txt_input.text)
        self.ids.txt_display.add_text(self.ids.txt_input.text)
        self.update()
        self.ids.txt_input.text = ""
        Clock.schedule_once(self.refocus_txtinput)

    def update(self):
        read(self.ids.txt_display, self.player, self.ids.txt_input.text)
        self.update_display()

    def update_display(self):
        self.ids.info_box.get_player_stats(self.player)
        self.ids.info_box.display_stats()

    def refocus_txtinput(self, *args, **kwargs):
        """Refocuses the cursor on the text input"""
        self.ids.txt_input.focus = True

class BackgroundImage(BoxLayout):
    pass

class TextDisplay(Label):
    """Text Display Widget"""
    def __init__(self, *args, **kwargs):
        super(TextDisplay, self).__init__(**kwargs)
        self.text_storage = []

    def add_text(self, text):
        """Adds text to the console"""
        self.text_storage.append(text)  #stores the text in a list
        text_string = ""
        if len(self.text_storage)>100: #if list has more than 100 entries, deletes the first entry to avoid display bugs
            del self.text_storage[0]

        for i in range(0, len(self.text_storage)):
            log = text_string
            text_string = "".join((log, str(self.text_storage[i]),"\n"))
            self.text = text_string
            print(self.text)
        print(len(self.text_storage))
        print(self.text_storage)




'''Minimap Widget'''
class MiniMapBox(RelativeLayout):
    def __init__(self, *args, **kwargs):
        super(MiniMapBox, self).__init__(**kwargs)
        self.spritesheet = Atlas('spritesheet.atlas')
#        print(self.spritesheet.textures.keys())
        self.decal_x = -88
        self.decal_y = -76
        for i in range(0,8):
            for j in range(0,7):
                        self.reveal_map(('('+str(i)+','+str(j)+')'), ((i*25)+self.decal_x,(j*25)+self.decal_y))



    def reveal_map(self, xy, *args, **kwargs):
        """displays coords xy of the minimap"""
        coordinates = ((int(xy[1])*25)+self.decal_x,(int(xy[3])*25)+self.decal_y)
        map_part = Image(texture=self.spritesheet[str(xy)], pos=coordinates)
        self.add_widget(map_part)


'''Character Informations Box'''
class CharacterInfosBox(RelativeLayout):
    def __init__(self, *args, **kwargs):
        super(CharacterInfosBox, self).__init__(**kwargs)
        self.spritesheet = Atlas('spritesheet.atlas')
        self.armor = False
        self.sword = False
        self.display_stats()

    def get_player_stats(self, player):
        self.armor = player.has_armor()
        self.sword = player.has_sword()

    def display_stats(self):
        self.clear_widgets()
        if self.armor:
            platearmor = Image(texture = self.spritesheet["platearmor"], pos=(0,0))
            self.add_widget(platearmor)
        else:
            clotharmor = Image(texture = self.spritesheet["clotharmor"], pos=(0,0))
            self.add_widget(clotharmor)
            
        if self.sword:
            sword = Image(texture = self.spritesheet["sword"], pos=(-20,-6))
            self.add_widget(sword)
