import websocket


def on_message(ws, message):
    print(message)

def on_close(ws):
    print("closed connection")

# socket =  'wss://fstream.binance.com/ws/bnbusdt@aggTrade'
# candlestick_streams =  'wss://fstream.binance.com/ws/bnbusdt@kline_1m'
# orderbook_streams = 'wss://fstream.binance.com/ws/bnbusdt@bookTicker'
# ws = websocket.WebSocketApp(candlestick_streams, on_message=on_message, on_close=on_close)
# ws.run_forever()


class BinanceSockets:
    def __init__(self, socket_URL):
        self.URL = socket_URL

    def stream(self, strategy):
        ws = websocket.WebSocketApp(self.URL, on_message=strategy, on_close=on_close)
        self.content = ws.run_forever()

# https://binance-docs.github.io/apidocs/spot/en/#live-subscribing-unsubscribing-to-streams
# 1m
# 3m
# 5m
# 15m
# 30m
# 1h
# 2h
# 4h
# 6h
# 8h
# 12h
# 1d
# 3d
# 1w
# 1M
# Output format {"e":"kline","E":1649758390267,"s":"BNBUSDT","k":{"t":1649758380000,"T":1649758439999,"s":"BNBUSDT","i":"1m","f":672944526,"L":672944538,"o":"407.300","c":"407.290","h":"407.300","l":"407.290","v":"7.58","n":13,"x":false,"q":"3087.29790","V":"3.97","Q":"1616.98100","B":"0"}}