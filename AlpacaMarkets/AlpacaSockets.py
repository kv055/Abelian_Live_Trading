import websocket, json

APCA_API_KEY_ID = 'AKTY9EUCRJZWTAIQVKQR'
APCA_API_SECRET_KEY = 'Beynq6kJ4aCapM3E6xRH5BDhziFzuMaxyCTjMwIq'

def on_open(ws):
    print("opened")
    auth_data = {
        "action": "auth",
        "key": APCA_API_KEY_ID, 
        "secret": APCA_API_SECRET_KEY
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


socket = 'wss://stream.data.alpaca.markets/v2/iex'

ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)
ws.run_forever()