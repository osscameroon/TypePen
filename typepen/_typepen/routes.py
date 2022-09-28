import os
import time

from flask import render_template, url_for
from typepen._typepen import server

PATH_TO_ALL_FILES = "C:\\Users\\HanslettTheDev\\Documents\\loks"

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
    print(content)
    return render_template('open_note.html', content=content)


@server.route('/edit/<file_name>')
def edit_notes(file_name:str):
    with open(os.path.join(PATH_TO_ALL_FILES, file_name), "r") as file:
        content = file.read()
    return render_template('edit.html', content=content)


# @server.route('/delete/<file_name>')
# def delete_note():
#     return