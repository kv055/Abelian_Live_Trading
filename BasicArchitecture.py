import os
from dotenv import load_dotenv

from Kraken.Kraken_Connector import KrakenSpot
from Strategies.DummyStrategy import DumbStrategy
from Fetch_OHLC import get_price

load_dotenv()

# Load KRAKEN Keys

PRIV = os.getenv('KRAKEN_PRIV_KEY')
PUB = os.getenv('KRAKEN_PUB_KEY')

# Init Kraken Connection
kraken_connection = KrakenSpot(PUB,PRIV)

# Init strategies
TEST_strategy = DumbStrategy(kraken_connection)


# Fetch PriceData
lol = get_price('https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT')

# execute
TEST_strategy.load_pricedata(lol)
TEST_strategy.trade()
lol = 0