import webview
from typepen._typepen.api import API

class CreateWindow:
    def __init__(self, title:str="TypePen", server=None, gui_type:str="edgechromium", window_frame:bool=False, debug:bool=False, width:int=642, 
    height:int=300, js_api = None):
        self.__window_gui = gui_type
        self.__window_server = server
        self.__window_title = title
        self.__window_frame = window_frame
        self.__window_debug = debug
        self.__window_object:webview.Window = None
        self.__window_height = height
        self.__window_width = width
        self.__window_js_api = js_api

    def initWindow(self):
        self.__window_object = webview.create_window(
            self.__window_title,
            url=self.__window_server,
            frameless= self.__window_frame,
            width= self.__window_width,
            height=self.__window_height,
            js_api=self.__window_js_api
        )

        webview.start(
            gui = self.__window_gui,
            debug = self.__window_debug
        )
    
    def sizeGui(self, width:int, height:int):
        self.__window_object.resize(width,height)

    def moveGui(self,x:int,y:int):
        self.__window_object.move(x,y)