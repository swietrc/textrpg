# -*- coding: UTF-8 -*-

from gui import *
import kivy
kivy.require('1.8.0')

from kivy.app import App


'''Main App Class'''
class TextRPGApp(App):
	
	def build(self):
		game = Game()
		return game
    
if __name__ == '__main__':
	TextRPGApp().run()
