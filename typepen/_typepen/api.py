import webview
import os
import configparser
from typepen.create_config import CreateConfig
from typepen import config

class API:
	def __init__(self):
		self.windows:list = webview.windows
		self.typepen_config = CreateConfig()
		self.config = configparser.ConfigParser()

	def close_window(self):
		# Kill child windows first
		for window in self.windows:
			if self.windows.index(window) == 0:
				continue
			window.destroy()

		self.windows[0].destroy()

	def minimize_window(self):
		self.windows[0].minimize()
	
	def new_window(self):
		if len(self.windows) == 2:
			return False
		window2 = webview.create_window('TypePen - New Note', width=900, height=700, min_size=(700,690))
		window2.load_url(self.windows[0].get_current_url() + "/new")

	def save_file(self, file_name:str, info:str) -> str:
		window = webview.create_window("")
		window.hide()
		file_path = window.create_file_dialog(webview.SAVE_DIALOG, save_filename=f"{file_name}.typen")
		if file_path:
			with open(file_path, "w") as file:
				file.write(info)
		window.destroy() # destroys the window after saving the file
		
		if os.path.exists(file_path):
			return True

	def save_settings(self, new_settings:dict=None):
		''' This function can be scalled but for now it will use the hardcoded settings value '''
		# The state is used for the toggle on and off button 
		# the settings variable will be used only for options which need to pass some extra data

		print(new_settings)

		if new_settings:
			self.typepen_config.update_config_file("TypePenSettings", new_settings)
	
	def load_settings(self):
		''' loop through all the setting names and get their corresponding keys and values
			This is for future scaling of the application if there is an increase in settings configurations
		 '''
		settings = {}
		self.config.read(config.CF_NAME)

		for cfname in config.CF_SETTING_NAMES:
			for key, value in self.config[cfname].items():
				settings[key] = value

		return settings

	def settings_path(self):
		swindow = webview.create_window("")
		swindow.hide()
		folder_path = swindow.create_file_dialog(webview.FOLDER_DIALOG)
		swindow.destroy()
		return folder_path[0]

	def open_file(self):
		file_types = ('Typen Files (*.typen;*.typen;*.typen)', 'All files (*.*)')
		window = webview.create_window("")
		window.hide()
		file_path = window.create_file_dialog(webview.OPEN_DIALOG, file_types=file_types)
		window.destroy()

		if os.path.exists(file_path[0]):
			return file_path[0].split('\\')[-1]
	
	def open_file_window(self, file_name:str):
		window = webview.create_window(f'TypePen - {file_name}', width=900, height=700, min_size=(700,690))
		window.load_url(self.windows[0].get_current_url() + f"/new/{file_name}")


	def delete_file(self, file_url:str):
		os.remove(os.path.join(file_url))
		if not os.path.exists(os.path.join(file_url)):
			return True

	def settings_window(self):
		window = webview.create_window("TypePen - Settings", width=450, height=300, resizable=False, js_api=API())
		window.load_url(self.windows[0].get_current_url() + "/settings")