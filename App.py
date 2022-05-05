import os
from dotenv import load_dotenv

from AlpacaMarkets.AlpacaConnector import Alpaca
from AlpacaMarkets.AlpacaSockets import AlpacaSockets

from Binance.BinanceSpotConnector import BinanceSpot
from Binance.BinanceSockets import BinanceSockets

from Strategies.DummyStrategy import DumbStrategy

load_dotenv()

# Database Architecture:
# Client:
# Id: int, Name: string, Keys: [{Exchange: Binance, Priv:xxxx, Pub: yyyyy}], 
# Assets[{Exchange: Kraken, Ticker:BTCUSDT, Timeframe: 1d}], 
# Strategies [{Strat:MACrossings, Parameter: 5 vs 10}]

# for ClientID in Customers:
#   load keys 
#   instanciate connection to Exchange
#   get Ohlc Data 
#   execute all selected strategies
#   work out how relational connections work and implement them
Config_Sets = [
    {'ID': 69,'Acc_Keys_ID': 420,'Strategy_ID': 7,'Asset_ID': 4,'Timeframe': '1d'},
    {'ID': 70,'Acc_Keys_ID': 420,'Strategy_ID': 7,'Asset_ID': 5,'Timeframe': '4h'},
    {'ID': 71,'Acc_Keys_ID': 420,'Strategy_ID': 19,'Asset_ID': 5,'Timeframe': '4h'},
    {'ID': 72,'Acc_Keys_ID': 420,'Strategy_ID': 19,'Asset_ID': 22,'Timeframe': '15m'},
    {'ID': 73,'Acc_Keys_ID': 421,'Strategy_ID': 19,'Asset_ID': 5,'Timeframe': '4h'},
    {'ID': 74,'Acc_Keys_ID': 421,'Strategy_ID': 7,'Asset_ID': 67,'Timeframe': '1m'}
]

# Since Strategy is executing

globalStrategies = []
# for DISTINCT_Strategy_ID in Config_Sets:
#     # globalStrategies.append(Strategy)

globalConnections = []
# for entry in Config_Sets:
    # get key pairs
    # init connections
    # globalConnections.append(connection)


# for JOIN DISTINCT_Strategy_ID and corresponding key ids:
    # init Strategy
    # pick matching PriceDataConfig

globalPriceData = []
# for DISTINCT_Asset_ID / TimeFrame_ID config in Config_Sets:
    # fetch price_data




# Load Alpaca Keys
ALPACA_PAPERTRADING_PUB_KEY = os.getenv('ALPACA_PAPERTRADING_PUB_KEY')
ALPACA_PAPERTRADING_PRIV_KEY = os.getenv('ALPACA_PAPERTRADING_PRIV_KEY')

ALPACA_PUB_KEY = os.getenv('ALPACA_PUB_KEY')
ALPACA_PRIV_KEY = os.getenv('ALPACA_PRIV_KEY')

# Init Alpaca Connection
# Endpoints
APCA_API_BASE_URL =	'https://api.alpaca.markets' 
APCA_API_DATA_URL = 'https://data.alpaca.markets'
APCA_API_PAPERTRADING_URL = 'https://paper-api.alpaca.markets'

alpaca_connection = Alpaca(
    ALPACA_PAPERTRADING_PUB_KEY,
    ALPACA_PAPERTRADING_PRIV_KEY,
    APCA_API_PAPERTRADING_URL)

# init Strategy
alpaca_strategy = DumbStrategy(alpaca_connection)
alpaca_strategy.trade()

# Init Stream
socket = 'wss://stream.data.alpaca.markets/v2/iex'
alpaca_wss = AlpacaSockets(
    ALPACA_PUB_KEY,
    ALPACA_PRIV_KEY,
    socket
)
alpaca_wss.stream()

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
