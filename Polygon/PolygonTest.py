import websocket, json

def on_open(ws):
    print("opened")
    auth_data = {
        "action": "auth",
        "params":"CZHNqkB7KhkX17BmTopnKYyqQ7Y15EbR"
    }

    ws.send(json.dumps(auth_data))
    listen_message = {
        "action":"subscribe",
        "trades":["AAPL"],
        "quotes":["AMD","CLDR"],
        "bars":["AAPL","VOO"]
    }

    ws.send(json.dumps(listen_message))


def on_message(ws, message):
    # print("received a message")
    print(message)

def on_close(ws):
    print("closed connection")


socket = 'wss://socket.polygon.io/stocks'

ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)
ws.run_forever()