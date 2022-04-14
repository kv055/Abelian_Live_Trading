import os
from dotenv import load_dotenv

load_dotenv()

# Exchange connectors

# Alpaca
from AlpacaMarkets.AlpacaClass import Alpaca
# from AlpacaMarkets.AlpacaSockets import 

# Binance
from Binance.BinanceSpotClass import BinanceSpot
# from Binance.BinanceSockets import 

# Load Environement Variables
ALPACA_PAPERTRADING_PUB_KEY = os.getenv('ALPACA_PAPERTRADING_PUB_KEY')
ALPACA_PAPERTRADING_PRIV_KEY = os.getenv('ALPACA_PAPERTRADING_PRIV_KEY')

# Strategies

# Todo: 
# Code Bullshit Strategy and deploy it here
