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
    def __init__(self, *args, **kwargs):
        Character.__init__(self)
        self.name = "John Doe"          # player name
        self.hp = 100                   # player health
        self.maxhp = 100                # player max health
        self.armor = 0                  # player armor
        self.sword = False              # player has a sword
        self.xposition = 0              # x location of the player
        self.yposition = 0              # y location of the player
        self.turns = 0                  # amount of turns played

    def is_alive(self, *args, **kwargs):
        """returns True if the player is alive"""
        if self.hp>0:
            return True
        else:
            return False

    def move(self, widget, direction, *args, **kwargs):
        """changes the position of the player"""

        if direction == 'N' or direction == 'NORD':
            if (self.yposition+1) <= 6:
                self.yposition += 1
        elif direction == 'S' or direction == 'SUD':
            if (self.yposition-1) >= 0:
                self.yposition -= 1
        elif direction == 'E' or direction == 'EST':
            if (self.xposition+1) <= 7:
                self.xposition += 1
        elif direction == 'O' or direction == 'OUEST':
            if (self.xposition-1) >= 0:
                self.xposition -= 1

    def add_hp(self, hp, *args, **kwargs):
        """Adds health points to the player"""
        hp=int(hp)
        if self.hp+hp <= self.maxhp:
            self.hp = self.hp+hp
        else:
            self.hp = self.maxhp

    def add_armor(self, armor, *args, **kwargs):
        """Adds armor points to the player"""
        armor=int(armor)
        self.armor = self.armor+armor

    def get_stats(self, widget, *args, **kwargs):
        widget.add_text("Vie: "+str(self.hp)+"\nArmure: "+str(self.armor)+"\nPosition: "+str(self.xposition)+", "+str(self.yposition))

    def has_armor(self, *args, **kwargs):
        """returns True if player has armor points"""
        if self.armor>0:
            return True
        else:
            return False

    def has_sword(self, *args, **kwargs):
        """returns True if player has a sword"""
        if self.sword == True:
            return True
        else:
            return False

    def get_pos(self, *args, **kwargs):
        """returns the position of player"""
        return (self.xposition,self.yposition)

    def get_hp(self, *args, **kwargs):
        """returns the health points of the player"""
        return self.hp

    def get_armor(self, *args, **kwargs):
        """returns the armor of a player"""
        return self.armor

    def find_armor(self, *args, **kwargs):
        """adds 20 armor points to player"""
        self.add_armor(20)

    def find_food(self, *args, **kwargs):
        """adds 50 health points to player"""
        self.add_hp(50)

    def do_damage(self, enemy, *args, **kwargs):
        """calculates the amount of damage inflicted by player to enemy"""
        if self.sword == True:
            damage_player=int(random.triangular(7,10))
            enemy.hp -= damage_player
            return enemy.hp
        else:
            damage_player=int(random.triangular(3,7))
            enemy.hp -= damage_player
            return enemy.hp


class Enemy(Character):
    def __init__(self, *args, **kwargs):
        Character.__init__(self)
        self.name = "Ugly Goblin"
        self.hp = 20

    def do_damage(self, player, *args, **kwargs):
        damage_enemy=int(random.triangular(2,5))
        player.hp -= damage_enemy