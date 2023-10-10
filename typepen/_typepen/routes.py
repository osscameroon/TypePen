import os
import time

from flask import render_template, url_for
from typepen._typepen import server

PATH_TO_ALL_FILES = "C:\\Users\\Dell\\Documents\\loks"

if not os.path.exists(PATH_TO_ALL_FILES):
    os.mkdir(PATH_TO_ALL_FILES)

@server.route('/')
def home():
    all_dir_files = os.listdir(PATH_TO_ALL_FILES)
    file_details = {}
    for adf in all_dir_files:
        if adf.endswith('.typen'):
            file_details[adf] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime(os.path.join(PATH_TO_ALL_FILES, adf))))
    
    return render_template('main.html', file_details=file_details, dpath=PATH_TO_ALL_FILES)

@server.route('/new')
def new_note():
    return render_template('new_file.html')

@server.route('/new/<file_name>')
def open_note(file_name:str):
    with open(os.path.join(PATH_TO_ALL_FILES, file_name)) as file:
        content = file.read()
    return render_template('new_file.html', content=content)


@server.route('/edit/<file_name>')
def edit_notes(file_name:str):
    with open(os.path.join(PATH_TO_ALL_FILES, file_name), "r") as file:
        content = file.read()
    return render_template('edit.html', content=content)


@server.route('/settings')
def typepen_settings():
    return render_template('settings.html')
