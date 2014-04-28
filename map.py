#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from gui import *
import json

def load_json(file):
    return json.loads(open(file).read())

class MapTile():
    def __init__(self):
        self.tile_infos = load_json("story.json")
        print(self.tile_infos)

tile = MapTile()


