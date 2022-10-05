import webview
import os

html = '''
<div class="main-container">
    <div id="loader" class="loading-container">
        <div class="loader">Loading...</div>
    </div>

    <div id="main" class="loaded-container">
        <button type="button" id="back"><a href="{{ url_for('home') }}">Back</a></button>
<div class="text-content" contenteditable="true"></div>
<div class="button-container" id="buttons">
    <button id="bold1" class="btn" >B</button>
    <button class="btn" id="ita">I</button>
    <button class="btn" id="underline-btn">U</button>
    <button id="save-text">Save Note</button>
</div>
    </div>
</div>

'''

class API:
    def close_window(self):
        # webview.windows[0].destroy()
        # destroy all webview windows 
        for window in webview.windows:
            window.destroy()

    def minimize_window(self):
        webview.windows[0].minimize()
    
    def new_window(self):
        window2 = webview.create_window('TypePen - New Note', width=900, height=700, min_size=(700,690))
        window2.load_url(webview.windows[0].get_current_url() + "/new")


    def get_file_details(self, file_details:str):
        print(file_details)
        return "details received"

    def save_file(self, file_name:str, info:str) -> str:
        window = webview.create_window("")
        window.hide()
        file_path = window.create_file_dialog(webview.SAVE_DIALOG, save_filename=f"{file_name}.typen")
        if file_path:
            with open(file_path, "w") as file:
                file.write(info)
        window.destroy() # destroys the window after saving the file
        
        if os.path.exists(file_path):
            return "Saved"
    
    def open_file(self):
        file_types = ('Typen Files (*.typen;*.typen;*.typen)', 'All files (*.*)')
        window = webview.create_window("")
        window.hide()
        file_path = window.create_file_dialog(webview.OPEN_DIALOG, file_types=file_types)
        window.destroy()

        if os.path.exists(file_path[0]):
            with open(file_path[0], "r") as file:
                return (file_path[0].split('\\')[-1], file.read())

    def delete_file(self, file_url:str):
        os.remove(os.path.join(file_url))
        if not os.path.exists(os.path.join(file_url)):
            return "Deleted"