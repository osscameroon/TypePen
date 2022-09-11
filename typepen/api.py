import webview
import os

class API:
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