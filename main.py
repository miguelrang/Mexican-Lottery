from kivymd.app import MDApp

from kivy.core.window import Window
Window.maximize()
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

import os

from Home import Home
from ShowDeck import ShowDeck

class WindowManager(ScreenManager):
	def __init__(self, **kwargs):
		super(WindowManager, self).__init__(**kwargs)


class main(MDApp):
	def build(self):
		wm = WindowManager()
		wm.add_widget(Builder.load_file('Home.kv'))
		wm.add_widget(Builder.load_file('ShowDeck.kv'))
		
		return wm
		

	def on_start(self):
		global app
		app = MDApp.get_running_app()

		##

	def on_stop(self):
		os.system(f'rmdir /s /q images')


if __name__ == '__main__':
	main().run()