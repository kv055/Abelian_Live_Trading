import os
from re import I
from dotenv import load_dotenv
import time

# from Database_SQL.querry import querry
load_dotenv()

# Import Database Connection
from Database_SQL.aws_sql_connect import AWS_SQL, DummyData

# Import Query functions
from Database_SQL.querry_config import config_live_trading 
# from Database_SQL.query_kraken_assets import kraken_assets
# from Database_SQL.query_binance_assets import binance_assets

# Import live data fetch modules
# from Binance.FetchLiveData import live_price_data_Binance
# from Kraken.FetchLiveData import live_price_data_Kraken
# from Alpaca.FetchLiveData import live_price_data_Alpaca
from Test_Data.Test_Data import PriceDataFetch

# Import connections
# from Database_SQL.create_connectors import connector_instances
from Binance.BinanceSpotConnector import BinanceSpot
from AlpacaMarkets.AlpacaConnector import Alpaca

# Import Strategies
# from Strategies.DummyStrategy import DumbStrategy
from Test_Data.DummyStrategy_No_LOOP import DumbStrategy

# Conecting to DB
# connection = AWS_SQL(load_dotenv)
connection = DummyData(load_dotenv)

# Fetch all assets from Config module
# querry_from = config_live_trading(connection)
# config_rows_DB = querry_from.Join()

# id, user_id, strategy_id, asset_id, trade_start, keys_id
config_rows_DB = ['1', '36', '1', '2578', 'NULL', '18']


# connectors = connector_instances(config_rows_DB)
# connectors = BinanceSpot()
connectors = Alpaca(
    'PK0RPI7F5X8M0VVED26I',
    '6VoDwGzKZ3uvPPq8awfspLesuYDnPqYtx0ZhPefG',
    'https://paper-api.alpaca.markets'
)
# Init all Strategies
test_strategy = DumbStrategy(config_rows_DB, connectors)
# test_strategy2 = DumbStrategy(config_rows_DB, connectors)

# every 5min execute
# ask Steele on how reliable that shit is
i = 0
while i < 10000:

    # fetch price_Data
    all_price_data = PriceDataFetch()
    # make function universal, not just for binance
    
    # feed pricedata to Strategies
    test_strategy.load_pricedata(all_price_data)
    # test_strategy2.load_pricedata(all_price_data)

    # execute the trades
    test_strategy.trade_loop()

    # implement sleep function here
    time.sleep(600)
    i+=1



