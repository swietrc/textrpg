#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''Player Class'''

import random

class Character:
    def __init__(self):
        self.name = ""
        self.hp = 1
        self.maxhp = 1


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

    def move(self, widget, direction, *args, **kwargs):
        if direction == 'N' or direction == 'NORD':
            self.xposition += 1
        elif direction == 'S' or direction == 'SUD':
            self.xposition -= 1
        elif direction == 'E' or direction == 'EST':
            self.yposition += 1
        elif direction == 'O' or direction == 'OUEST':
            self.yposition -= 1

    def add_hp(self, hp):
        """Adds health points to the player"""
        hp=int(hp)
        if self.hp+hp <= self.maxhp:
            self.hp = self.hp+hp
        else:
            self.hp = self.maxhp

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

    def do_damage(self,Enemy):
        if self.sword==True:
            damage_player=int(random.triangular(7,10))
            #random.triangular c'est fantastique, la proba du médian est supérieur à la proba des extrémités
            Enemy.hp -= damage_player
            return Enemy.hp
        else:
            damage_player=int(random.triangular(3,7))
            Enemy.hp -= damage_player
            return Enemy.hp


class Enemy(Character):
    def __init__(self):
        Character.__init__(self)
        self.name = "vilain"
        self.hp=20

    def do_damage(self,player):
        damage_enemy=int(random.triangular(2,5))
        player.hp -= damage_enemy
        return player.hp




