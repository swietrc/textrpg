#!/usr/bin/env python
# -*- coding: UTF-8 -*-

food_dictionary={"bread":5,"fish":7, "apple":2,"potion":15}
armor_dictionary={"helmet":5, "cheat":999}

'''définition de la classe joueur'''

class Character:
    def __init__(self):
        self.name = ""
        self.hp = 1
        self.maxhp = 1

    def do_damage(self, enemy):
        damage = min(max(randint(0, self.hp) - randint(0, enemy.health), 0), enemy.health)
        enemy.hp -= damage

class Player(Character):
    def __init__(self):
        Character.__init__(self)
        self.name="John Doe"
        self.hp=100 #The players health
        self.maxhp=100 #The players max health
        self.ap=6 #?
        self.armor=0 #The players armor
        self.xposition=0 #The x location of the player
        self.yposition=0  #The y location of the player
        self.sword=False #If the player has a sword
        self.shield=False #If the player has a shield
        self.turns=0 #The amount of turns the player has had

    def add_hp(self,hp):
        """Adds health points to the player"""
        hp=int(hp)
        if self.hp+hp<=self.maxhp:
            self.hp = self.hp+hp
        else:
            self.hp=self.maxhp

    def add_armor(self,armor):
        """Adds armor points to the player"""
        armor=int(armor)
        self.armor = self.armor+armor

    def eat(self,food):
        food_value=food_dictionnary[food]
        self.add_hp(food_value)

    def equip(self,armor):
        armor_value=armor_dictionnary[armor]
        self.add_armor(armor_value)

    def get_stats(self, widget, *args, **kwargs):
        widget.add_text("Vie: "+str(self.hp)+"\nArmure: "+str(self.armor)+"\nPosition: "+str(self.xposition)+", "+str(self.yposition))
 
        


class Enemy(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = "Ugly Troll"



