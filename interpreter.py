#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#command reader

import gui


pronouns = ['LE', 'LA',
           'LES', 'AU',
           'EN']

#retourne une liste des mots dans la chaine
def split_string(text):
    text = text.upper()
    return text.split(' ')

#retourne un tableau sans pronoms
def del_pronouns(text):
    for i in range(len(text)-1):
        if text[i] in pronouns:
            del text[i]
    return text

def read(display, player, text):
    commands = {"STATS": player.get_stats,
                "ALLER": player.move}

    args = split_string(text)
    args = del_pronouns(args)
    
    if args[0] in commands:
        if len(args) > 1:
            commands[args[0]](display, args[1])
        elif len(args) == 1:
            commands[args[0]](display)
        else:
            print("Error Interpreter")