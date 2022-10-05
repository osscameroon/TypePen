import webview
from typepen._typepen import server
from typepen._typepen.api import API

if __name__ == '__main__':
    api = API()
    # app = CreateWindow(server=server, debug=True, width=642, height=300, window_frame=True, js_api=api)
    # app.initWindow()
    # server.run(port="3000", debug=True)
    window = webview.create_window('TypePen - Home', server, width=642, height=300, js_api=api, frameless=True, confirm_close=True)
    webview.start(debug=True)
    