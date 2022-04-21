import os
from dotenv import load_dotenv

from AlpacaMarkets.AlpacaClass import Alpaca
# from AlpacaMarkets.AlpacaSockets import 

from Binance.BinanceSpotClass import BinanceSpot
from Binance.BinanceSockets import BinanceSockets

from Strategies.DummyStrategy import DumbStrategy

load_dotenv()

# Load Alpaca Keys
ALPACA_PAPERTRADING_PUB_KEY = os.getenv('ALPACA_PAPERTRADING_PUB_KEY')
ALPACA_PAPERTRADING_PRIV_KEY = os.getenv('ALPACA_PAPERTRADING_PRIV_KEY')

# Init Alpaca Connection
APCA_API_PAPERTRADING_URL = 'https://paper-api.alpaca.markets'
alpaca_connection = Alpaca(APCA_API_PAPERTRADING_URL)

# init Strategy
alpaca_strategy = DumbStrategy(alpaca_connection)
alpaca_strategy.trade()

# Init Stream


# -----------------------------------------


# Load Binance Keys
BINANCE_PUB_KEY = os.getenv('BINANCE_PUB_KEY')
BINANCE_PRIV_KEY = os.getenv('BINANCE_PRIV_KEY')

# Init Binance Connection
binance_connection = BinanceSpot(BINANCE_PUB_KEY,BINANCE_PRIV_KEY)

# Init strategies
binance_strategy = DumbStrategy(binance_connection)
binance_strategy.trade()

# Init Stream
candlestick_streams_URL = 'wss://fstream.binance.com/ws/bnbusdt@kline_1m'
trade_bnbusdt = BinanceSockets(candlestick_streams_URL)
trade_bnbusdt.stream(DumbStrategy)
