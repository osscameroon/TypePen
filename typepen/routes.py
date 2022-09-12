import os
import time


from flask import render_template,request
from typepen import server

#open user data directory create one if doen't exist
PATH_TO_ALL_FILES=os.getenv('APPDATA')+'/typepen'

if not os.path.exists(PATH_TO_ALL_FILES):#check if data directory exist
    os.makedirs(PATH_TO_ALL_FILES)#create a new data directory

#home
@server.route('/')
def home():
    all_dir_files = os.listdir(PATH_TO_ALL_FILES)
    file_details = {}
    for adf in all_dir_files:
        if adf.endswith('.typen'):
            file_details[adf] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime(os.path.join(PATH_TO_ALL_FILES, adf))))
    
    return render_template('main.html', file_details=file_details, dpath=PATH_TO_ALL_FILES)


@server.route('/editor',methods = ['GET'])
def edit_notes():
    content=str()
    filename=str()
    if request.method=='GET':
        print(request.form)
        if "open" in request.args.keys():
            filename=request.args.get("open")
            try:
                print(filename)
                with open(os.path.join(PATH_TO_ALL_FILES, filename), "r") as file:
                    content = file.read()     
            except:
                print("cannot open %s"%filename)
    else :
        content='add some content here'
        print('new file will be created')
    return render_template('edit.html', content=content)