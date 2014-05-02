# -*- coding: UTF-8 -*-a

from gui import *
import kivy
kivy.require('1.8.0')

from kivy.app import App



class TextRPGApp(App):
	"""Main App Class"""	
	def build(self):
		game = Game()
		return game
    
if __name__ == '__main__':
	TextRPGApp().run()
