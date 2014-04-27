#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''Player Class'''

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
        self.armor=0 #The players armor
        self.sword=False #If the player has a sword
        self.xposition=0 #The x location of the player
        self.yposition=0  #The y location of the player
        self.turns=0 #The amount of turns the player has had

    def is_alive(self):
        if self.hp>0:
            return True
        else:
            return False
    def add_hp(self,hp):
        """Adds health points to the player"""
        hp=int(hp)
        if self.hp+hp<=self.maxhp:
            self.hp = self.hp+hp
        else:
            self.hp=self.maxhp

    def add_armor(self, armor):
        """Adds armor points to the player"""
        armor=int(armor)
        self.armor = self.armor+armor

    def get_stats(self, widget, *args, **kwargs):
        widget.add_text("Vie: "+str(self.hp)+"\nArmure: "+str(self.armor)+"\nPosition: "+str(self.xposition)+", "+str(self.yposition))

    def has_armor(self):
        if self.armor>0:
            return True
        else:
            return False

    def has_sword(self):
        if self.sword == True:
            return True
        else:
            return False

    def get_pos(self):
        return (xposition, yposition)

    def get_hp(self):
        return self.hp

    def get_armor(self):
        return self.armor

    def find_armor(self):
        self.add_armor(20)

    def find_food(self):
        self.add_hp(50)
 
        
class Enemy(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = "Ugly Troll"



