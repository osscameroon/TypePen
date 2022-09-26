import os
import sys
from flask import Flask


def get_resource_path(relative_path:str):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath('.'), relative_path)


server = Flask(__name__, static_folder=get_resource_path('assets'), template_folder=get_resource_path('templates'))

from typepen import routes