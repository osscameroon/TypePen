import webview
from typepen import server
from typepen.api import API

if __name__ == '__main__':
    api = API()
    # server.run(port="3000")
    window = webview.create_window('TypePen', server, min_size=(900, 700), js_api=api)
    webview.start(debug=True)