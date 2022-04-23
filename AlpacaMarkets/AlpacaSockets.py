import websocket, json

class AlpacaSockets:
    def __init__(self, key, secr_key, socket_URL):
        self.URL = socket_URL
        self.auth_data = {
            "action": "auth",
            "key": key,
            "secret": secr_key
        }

    def stream(self):

        def on_open(ws):
            ws.send(json.dumps(self.auth_data))
            listen_message = {
                "action":"subscribe",
                "trades":["AAPL"],
                # "quotes":["AMD","CLDR"],
                # "bars":["AAPL","VOO"]
            }

            ws.send(json.dumps(listen_message))

        def on_message(ws, message):
            print("received a message")
            print(message)

        def on_close(ws):
            print("closed connection")
        

        ws = websocket.WebSocketApp(self.URL, on_open=on_open, on_message=on_message, on_close=on_close)
        ws.run_forever()