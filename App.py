import os
from dotenv import load_dotenv

from AlpacaMarkets.AlpacaConnector import Alpaca
from AlpacaMarkets.AlpacaSockets import AlpacaSockets

from Binance.BinanceSpotConnector import BinanceSpot
from Binance.BinanceSockets import BinanceSockets

from Strategies.DummyStrategy import DumbStrategy

load_dotenv()

# # Init Alpaca Connection
# # Endpoints
# APCA_API_BASE_URL =	'https://api.alpaca.markets' 
# APCA_API_DATA_URL = 'https://data.alpaca.markets'
# APCA_API_PAPERTRADING_URL = 'https://paper-api.alpaca.markets'

# alpaca_connection = Alpaca(
#     ALPACA_PAPERTRADING_PUB_KEY,
#     ALPACA_PAPERTRADING_PRIV_KEY,
#     APCA_API_PAPERTRADING_URL)

# # init Strategy
# alpaca_strategy = DumbStrategy(alpaca_connection)
# alpaca_strategy.trade()

# # Init Stream
# socket = 'wss://stream.data.alpaca.markets/v2/iex'
# alpaca_wss = AlpacaSockets(
#     ALPACA_PUB_KEY,
#     ALPACA_PRIV_KEY,
#     socket
# )
# alpaca_wss.stream()

# # -----------------------------------------

# # Init Binance Connection
# binance_connection = BinanceSpot(BINANCE_PUB_KEY,BINANCE_PRIV_KEY)

# # Init strategies
# binance_strategy = DumbStrategy(binance_connection)
# binance_strategy.trade()

# # Init Stream
# candlestick_streams_URL = 'wss://fstream.binance.com/ws/bnbusdt@kline_1m'
# trade_bnbusdt = BinanceSockets(candlestick_streams_URL)
# trade_bnbusdt.stream(DumbStrategy)



from Database_SQL.aws_sql_connect import AWS_SQL
test_connection = AWS_SQL(load_dotenv)

from Database_SQL.querry import querry
querry(test_connection)
