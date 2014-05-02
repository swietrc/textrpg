#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from gui import *
import json

def load_json(file):
    return json.loads(open(file).read())

class MapTile():
    def __init__(self):
        self.tile_infos = load_json("story.json")
        self.id = ""
        self.description = ""
        self.is_sword = False
        self.is_armor = False
        self.is_enemy = False
        self.is_boss = False
#        print(self.tile_infos)

    def update(self, player):
        try:
            key = str(player.xposition)+str(player.yposition)
            self.id = self.tile_infos[key]['id']
            self.description = self.tile_infos[key]['description']
            self.is_sword = self.tile_infos[key]['sword']
            self.is_armor = self.tile_infos[key]['armor']
            self.is_enemy = self.tile_infos[key]['enemy']
            self.is_boss = self.tile_infos[key]['boss']
        except:
            print("unable to load infos for coord "+key)




