from kivymd.app import MDApp
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.metrics import dp
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen
### IMAGES
from io import BytesIO
from kivy.uix.image import Image as IMG
from kivy.core.image import Image as CoreImage
###
from threading import Thread
import random
import os

from PIL import Image

import random


Builder.load_string(
'''
<Card>:
	MDGridLayout:
		cols: 1
		canvas.before:
			Color:
				rgb: (1, 1, 1)

			Rectangle:
				size: self.size
				pos: self.pos

		Image:
			allow_stretch: True
			texture: root.texture1

		MDLabel:
			text: '[b]{}[/b]'.format(root.label1)
			font_size: dp(10)
			size_hint_y: .1
			halign: 'center'
			valign: 'center'
			markup: True
	
	MDGridLayout:
		cols: 1
		canvas.before:
			Color:
				rgb: (1, 1, 1)

			Rectangle:
				size: self.size
				pos: self.pos
				
		Image:
			allow_stretch: True
			texture: root.texture2

		MDLabel:
			text: '[b]{}[/b]'.format(root.label2)
			font_size: dp(10)
			size_hint_y: .1
			halign: 'center'
			valign: 'center'
			markup: True
	
	MDGridLayout:
		cols: 1
	
		canvas.before:
			Color:
				rgb: (1, 1, 1)

			Rectangle:
				size: self.size
				pos: self.pos
				
		Image:
			allow_stretch: True
			texture: root.texture3

		MDLabel:
			text: '[b]{}[/b]'.format(root.label3)
			font_size: dp(10)
			size_hint_y: .1
			halign: 'center'
			valign: 'center'
			markup: True
	

	MDGridLayout:
		cols: 1
	
		canvas.before:
			Color:
				rgb: (1, 1, 1)

			Rectangle:
				size: self.size
				pos: self.pos
				
		Image:
			allow_stretch: True
			texture: root.texture4
		MDLabel:
			text: '[b]{}[/b]'.format(root.label4)
			font_size: dp(10)
			size_hint_y: .1
			halign: 'center'
			valign: 'center'
			markup: True
	
	MDGridLayout:
		cols: 1
		canvas.before:
			Color:
				rgb: (1, 1, 1)

			Rectangle:
				size: self.size
				pos: self.pos
				
		Image:
			allow_stretch: True
			texture: root.texture5

		MDLabel:
			text: '[b]{}[/b]'.format(root.label5)
			font_size: dp(10)
			size_hint_y: .1
			halign: 'center'
			valign: 'center'
			markup: True
	
	MDGridLayout:
		cols: 1
		canvas.before:
			Color:
				rgb: (1, 1, 1)

			Rectangle:
				size: self.size
				pos: self.pos
				
		Image:
			allow_stretch: True
			texture: root.texture6

		MDLabel:
			text: '[b]{}[/b]'.format(root.label6)
			font_size: dp(10)
			size_hint_y: .1
			halign: 'center'
			valign: 'center'
			markup: True
	
	MDGridLayout:
		cols: 1
		canvas.before:
			Color:
				rgb: (1, 1, 1)

			Rectangle:
				size: self.size
				pos: self.pos
				
		Image:
			allow_stretch: True
			texture: root.texture7
		MDLabel:
			text: '[b]{}[/b]'.format(root.label7)
			font_size: dp(10)
			size_hint_y: .1
			halign: 'center'
			valign: 'center'
			markup: True
	
	MDGridLayout:
		cols: 1
		canvas.before:
			Color:
				rgb: (1, 1, 1)

			Rectangle:
				size: self.size
				pos: self.pos
				
		Image:
			allow_stretch: True
			texture: root.texture8

		MDLabel:
			text: '[b]{}[/b]'.format(root.label8)
			font_size: dp(10)
			size_hint_y: .1
			halign: 'center'
			valign: 'center'
			markup: True
	
	MDGridLayout:
		cols: 1
		canvas.before:
			Color:
				rgb: (1, 1, 1)

			Rectangle:
				size: self.size
				pos: self.pos
				
		Image:
			allow_stretch: True
			texture: root.texture9

		MDLabel:
			text: '[b]{}[/b]'.format(root.label9)
			font_size: dp(10)
			size_hint_y: .1
			halign: 'center'
			valign: 'center'
			markup: True
	
	MDGridLayout:
		cols: 1
		canvas.before:
			Color:
				rgb: (1, 1, 1)

			Rectangle:
				size: self.size
				pos: self.pos
				
		Image:
			allow_stretch: True
			texture: root.texture10

		MDLabel:
			text: '[b]{}[/b]'.format(root.label10)
			font_size: dp(10)
			size_hint_y: .1
			halign: 'center'
			valign: 'center'
			markup: True
	
	MDGridLayout:
		cols: 1
		canvas.before:
			Color:
				rgb: (1, 1, 1)

			Rectangle:
				size: self.size
				pos: self.pos
				
		Image:
			allow_stretch: True
			texture: root.texture11

		MDLabel:
			text: '[b]{}[/b]'.format(root.label11)
			font_size: dp(10)
			size_hint_y: .1
			halign: 'center'
			valign: 'center'
			markup: True
	
	MDGridLayout:
		cols: 1
		canvas.before:
			Color:
				rgb: (1, 1, 1)

			Rectangle:
				size: self.size
				pos: self.pos
				
		Image:
			allow_stretch: True
			texture: root.texture12

		MDLabel:
			text: '[b]{}[/b]'.format(root.label12)
			font_size: dp(10)
			size_hint_y: .1
			halign: 'center'
			valign: 'center'
			markup: True
	
	MDGridLayout:
		cols: 1
		canvas.before:
			Color:
				rgb: (1, 1, 1)

			Rectangle:
				size: self.size
				pos: self.pos
				
		Image:
			allow_stretch: True
			texture: root.texture13

		MDLabel:
			text: '[b]{}[/b]'.format(root.label13)
			font_size: dp(10)
			size_hint_y: .1
			halign: 'center'
			valign: 'center'
			markup: True
	
	MDGridLayout:
		cols: 1
		canvas.before:
			Color:
				rgb: (1, 1, 1)

			Rectangle:
				size: self.size
				pos: self.pos
				
		Image:
			allow_stretch: True
			texture: root.texture14

		MDLabel:
			text: '[b]{}[/b]'.format(root.label14)
			font_size: dp(10)
			size_hint_y: .1
			halign: 'center'
			valign: 'center'
			markup: True
	
	MDGridLayout:
		cols: 1
		canvas.before:
			Color:
				rgb: (1, 1, 1)

			Rectangle:
				size: self.size
				pos: self.pos
				
		Image:
			allow_stretch: True
			texture: root.texture15

		MDLabel:
			text: '[b]{}[/b]'.format(root.label15)
			font_size: dp(10)
			size_hint_y: .1
			halign: 'center'
			valign: 'center'
			markup: True

	MDGridLayout:
		cols: 1
		canvas.before:
			Color:
				rgb: (1, 1, 1)

			Rectangle:
				size: self.size
				pos: self.pos
				
		Image:
			allow_stretch: True
			texture: root.texture16

		MDLabel:
			text: '[b]{}[/b]'.format(root.label16)
			font_size: dp(10)
			size_hint_y: .1
			halign: 'center'
			valign: 'center'
			markup: True
'''
)
class Card(MDGridLayout):
	texture1=ObjectProperty()
	label1=StringProperty()
	texture2=ObjectProperty()
	label2=StringProperty()
	texture3=ObjectProperty()
	label3=StringProperty()
	texture4=ObjectProperty()
	label4=StringProperty()
	texture5=ObjectProperty()
	label5=StringProperty()
	texture6=ObjectProperty()
	label6=StringProperty()
	texture7=ObjectProperty()
	label7=StringProperty()
	texture8=ObjectProperty()
	label8=StringProperty()
	texture9=ObjectProperty()
	label9=StringProperty()
	texture10=ObjectProperty()
	label10=StringProperty()
	texture11=ObjectProperty()
	label11=StringProperty()
	texture12=ObjectProperty()
	label12=StringProperty()
	texture13=ObjectProperty()
	label13=StringProperty()
	texture14=ObjectProperty()
	label14=StringProperty()
	texture15=ObjectProperty()
	label15=StringProperty()
	texture16=ObjectProperty()
	label16=StringProperty()

class Cards(MDFloatLayout, MDTabsBase):
	''''''

Builder.load_string(
'''
<Deck>:
    MDGridLayout:
		cols: 1
		canvas.before:
			Color:
				rgb: (1, 1, 1)

			Rectangle:
				size: self.size
				pos: self.pos

		Image:
			allow_stretch: True
			texture: root.texture

		MDLabel:
			text: '[b]{}[/b]'.format(root.label)
			font_size: dp(14)
			size_hint_y: .1
			halign: 'center'
			valign: 'center'
			markup: True
'''
)
class Deck(MDGridLayout):
	texture=ObjectProperty()
	label=StringProperty()

class Deck_(MDFloatLayout, MDTabsBase):
	''''''

class ShowDeck(Screen):
	def __init__(self, **kwargs):
		super(ShowDeck, self).__init__(**kwargs)
		global app
		app = MDApp.get_running_app()


	def setData(self, imgs:list, size:tuple, cards:int, minimum:int=None, maximum:int=None, *largs):
		def resize(img:str, size:tuple):
			print(img, size)
			imag = Image.open(img)
			imag = imag.resize(size, Image.ANTIALIAS)
			listed = img.split('/')
			imag.save("images/{}".format(listed[len(listed)-1]))

		def texture(img):
			with open(img, 'rb') as f:
				img_bytes = f.read()

			core_img = CoreImage(
				BytesIO(img_bytes),
				ext='png'
			)
			
			return core_img.texture

		def setCards(imgs, cards:int, max:int, min:int):
			#def replaceFigure(figure):
			#	return 1

			repeat_allowed = max != None and min != None
			for i in range(cards):
				figures = []
				repeated = 0
				max_fig_repeated:int = 0
				for j in range(16):
					while True:
						figure = random.choice(imgs)
						if repeat_allowed:
							if figure not in figures:
								figures.append(figure)
								break
							elif figures.count(figure) == 1 and repeated < max:
								figures.append(figure)
								repeated += 1
								break

						else: # not allowed
							if figure not in figures:
								# not repeated
								figures.append(figure)
								break

				if i % 2 != 0:
					color = (234/255, 218/255, 0, 1)
				else:
					color = (0, 3/255, 234/255, 1)
				
				if repeat_allowed == True and repeated < min:
					figures_copy = figures.copy()

					while True:
						fig_to_duplicate = random.choice(figures)
						figures_copy.remove(fig_to_duplicate)

						fig_to_replace = random.choice(figures_copy)
						repeated += 1

						if repeated == min:
							break

				self.ids.cards.ids.recycle_card.data.append(
					{
						'viewclass': 'Card',
						'size_hint_y': 1,#3.5,
						'cols': 4,
						'padding': (dp(5), dp(5), dp(5), dp(5)), 
						'spacing': dp(5),
						'md_bg_color': color,
						'texture1': texture('images/' + figures[0]),
						'label1': figures[0].replace('.png', '').replace('.jpg', ''),
						'texture2': texture('images/' + figures[1]),
						'label2': figures[1].replace('.png', '').replace('.jpg', ''),
						'texture3': texture('images/' + figures[2]),
						'label3': figures[2].replace('.png', '').replace('.jpg', ''),
						'texture4': texture('images/' + figures[3]),
						'label4': figures[3].replace('.png', '').replace('.jpg', ''),
						'texture5': texture('images/' + figures[4]),
						'label5': figures[4].replace('.png', '').replace('.jpg', ''),
						'texture6': texture('images/' + figures[5]),
						'label6': figures[5].replace('.png', '').replace('.jpg', ''),
						'texture7': texture('images/' + figures[6]),
						'label7': figures[6].replace('.png', '').replace('.jpg', ''),
						'texture8': texture('images/' + figures[7]),
						'label8': figures[7].replace('.png', '').replace('.jpg', ''),
						'texture9': texture('images/' + figures[8]),
						'label9': figures[8].replace('.png', '').replace('.jpg', ''),
						'texture10': texture('images/' + figures[9]),
						'label10': figures[9].replace('.png', '').replace('.jpg', ''),
						'texture11': texture('images/' + figures[10]),
						'label11': figures[10].replace('.png', '').replace('.jpg', ''),
						'texture12': texture('images/' + figures[11]),
						'label12': figures[11].replace('.png', '').replace('.jpg', ''),
						'texture13': texture('images/' + figures[12]),
						'label13': figures[12].replace('.png', '').replace('.jpg', ''),
						'texture14': texture('images/' + figures[13]),
						'label14': figures[13].replace('.png', '').replace('.jpg', ''),
						'texture15': texture('images/' + figures[14]),
						'label15': figures[14].replace('.png', '').replace('.jpg', ''),
						'texture16': texture('images/' + figures[15]),
						'label16': figures[15].replace('.png', '').replace('.jpg', '')
					}
				)		

		def setDeck(deck:list):
			i:int = 0
			for figure in deck:
				if i % 2 != 0:
					color = (234/255, 218/255, 0, 1)
				else:
					color = (0, 3/255, 234/255, 1)

				# 6.35 & 9.5
				self.ids.deck.ids.recycle_deck.data.append(
					{
						'viewclass': 'Deck',
						'size_hint_y': 1,
						'cols': 1,
						'padding': (dp(5), dp(5), dp(5), dp(5)), 
						'spacing': dp(5),
						'md_bg_color': color,
						'texture': texture('images/{}'.format(figure)),
						'label': figure.replace('.png', '').replace('.jpg', '')
					}
				)
				i += 1


		try:
			os.mkdir('images')
		except:
			pass

		if size != ():
			os.system('mkdir images')
			for img in imgs:
				resize(img=img, size=size)
			
		else:
			directory = imgs[0].split('/')
			if '.png' in directory[len(directory)-1]:
				directory = imgs[0].replace(directory[len(directory)-1], '')
			
			os.system('copy "{}" "{}\\images"'.format(directory.replace('/', '\\'), os.getcwd()))

		setCards(
			imgs=os.listdir('images'),
			cards=cards,
			max=maximum,
			min=minimum
		)
		setDeck(
			deck=os.listdir('images')
		)
		app.root.current='showDeck'
					

