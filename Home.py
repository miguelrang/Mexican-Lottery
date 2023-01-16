from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton

from kivy.uix.screenmanager import Screen
from kivy.utils import platform
### IMAGES
from io import BytesIO
from kivy.uix.image import Image
from kivy.core.image import Image as CoreImage
###
from threading import Thread
from kivy.clock import Clock
from functools import partial
import os
import re


class Home(Screen):
	def __init__(self, **kwargs):
		super(Home, self).__init__(**kwargs)
		global app
		app = MDApp.get_running_app()

		# Initialize self.directory to choose an image (if it is necesary).
		self.directory = MDFileManager(
			select_path=self.selectFileFromDirectory,
			exit_manager=self.exitFromDirectory,
			preview=True
		)


	# IN CASE WE WILL CHOOSE AN IMAGE...
	def selectFileFromDirectory(self, path:str):
		file_format = re.compile(r'(.)+\.[a-z]+')
		path:str = path.replace('\\', '/')
		listed_path = path.split('/')
		last = listed_path[len(listed_path)-1]
		if last == '':
			last = listed_path[len(listed_path)-2]

		if file_format.fullmatch(last):
			path = path.replace(last, '')
		
		files = os.listdir(path)
		valid_list = True
		try:
			inv_file = None
			for file in files:
				if not (file.split('.')[1] in ['png', 'jpg'] and len(file.split('.')) == 2):
					inv_file = file
					valid_list = False
					break
		except:
			valid_list = False

		if valid_list:
			self.ids.folder.text = path
			self.exitFromDirectory()
		else:
			self.ids.folder.text = ''
			text = 'Su carpeta solo debe de contener imagenes de formato \'jpg\' or \'png\'.'
			if inv_file != None:
				text += ' Archivo invalido ({})'.format(inv_file)
			self.openDialog(
				title='Directorio Invalido.', 
				text=text
			)
				
			
	def exitFromDirectory(self, *args):
		self.directory.close()


	def openDirectory(self):
		if platform == 'win':
			if self.ids.folder.text == '':
				self.directory.show('/Users')
			else:
				self.directory.show(self.ids.folder.text)

		else:
			self.directory.show('/home/')
	
	##
	def openDialog(self, title:str, text:str):
		def closeDialog(*args):
			self.dialog.dismiss()

		self.dialog = MDDialog(
			title=title,
			text=text,
			buttons=[
				MDRectangleFlatButton(
					text='Aceptar',
					on_press=closeDialog
				)
			]
		)
		self.dialog.open()


	def showDeck(self, folder:str, height:str, width:str, n_cards:str, minimum_repeated:str, maximum_repeated:str, allow:bool):
		def loading(value, *largs):
			self.ids.loading.active=value

		if folder != '':
			if n_cards != '':
				imgs = []
				for img in os.listdir(folder):
					imgs.append("{}/{}".format(folder, img))
				if allow == True:
					if minimum_repeated != '' and maximum_repeated != '':
						if int(minimum_repeated) <= int(maximum_repeated):
							if int(minimum_repeated) > 0 and int(maximum_repeated) < 9:
								Clock.schedule_once(partial(loading, True), -1)
								if height != '' and width != '':
									Clock.schedule_once(
										partial(
											app.root.get_screen('showDeck').setData,
											imgs,
											(int(width), int(height)),
											int(n_cards),
											int(minimum_repeated),
											int(maximum_repeated)
										),
										1
									)
								else:
									Clock.schedule_once(
										partial(
											app.root.get_screen('showDeck').setData,
											imgs,
											(),
											int(n_cards),
											int(minimum_repeated),
											int(maximum_repeated)
										),
										1
									)
							else:
								self.openDialog(
									title='Atención',
									text='El número debe de ser mayor que 0 y menor que 9.'
								)
						else:
							self.openDialog(
								title='Atención',
								text='El número máximo es menor que el número minimo.'
							)
						
					else:
						self.openDialog(
							title='Atención',
							text='Debe especificar el número de casos de figuras repetidas.'
						)
				else:
					Clock.schedule_once(partial(loading, True), -1)
					if height != '' and width != '':
						Clock.schedule_once(
							partial(
								app.root.get_screen('showDeck').setData,
								imgs,
								(int(width), int(height)),
								int(n_cards)
							),
							1
						)
					else:
						Clock.schedule_once(
							partial(
								app.root.get_screen('showDeck').setData,
								imgs,
								(),
								int(n_cards)
							),
							1
						)
					
			else:
				self.openDialog(
					title='Atención',
					text='Debe especificar el número de tarjetas.'
				)
		else:
			self.openDialog(
					title='Atención',
					text='Debe especificar carpeta donde tiene sus imagenes.'
				)

		loading(False)