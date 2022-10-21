import webview
import os
from typepen._typepen import server
from typepen._typepen.api import API
from typepen.create_config import CreateConfig
from typepen import config


if __name__ == '__main__':
    # Create the typepen default folder for first time use 
    # Except user changes it later

    if not os.path.exists(config.DEFAULT_STORAGE_LOCATION):
        os.mkdir(config.DEFAULT_STORAGE_LOCATION)

    # Create the config file on first launch
    typepen_config = CreateConfig()
    if not os.path.exists(os.path.join(os.getcwd(), config.CF_NAME)):
        typepen_config.create_config_file("TypePenSettings", config.CF_DEFAULT)
    
    api = API()
    window = webview.create_window('TypePen - Home', server, width=642, height=300, js_api=api, frameless=True, confirm_close=True)
    webview.start(debug=True)
    