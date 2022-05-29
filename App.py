import os
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
from Binance.FetchLiveData import live_price_data_Binance
# from Kraken.FetchLiveData import live_price_data_Kraken
# from Alpaca.FetchLiveData import live_price_data_Alpaca

# Import connections
from Database_SQL.create_connectors import connector_instances

# Import Strategies
from Strategies.DummyStrategy import DumbStrategy

# Conecting to DB
# connection = AWS_SQL(load_dotenv)
connection = DummyData(load_dotenv)

# Fetch all assets from Config module
querry_from = config_live_trading(connection)
config_rows_DB = querry_from.Join()

connectors = connector_instances(config_rows_DB)

# Init all Strategies
test_strategy = DumbStrategy(config_rows_DB, connectors)
# test_strategy2 = DumbStrategy(config_rows_DB, connectors)

# every 5min execute
# ask Steele on how reliable that shit is
while True:

    # fetch price_Data
    all_price_data = live_price_data_Binance()
    # make function universal, not just for binance
    
    # feed pricedata to Strategies
    test_strategy.load_pricedata(all_price_data)
    # test_strategy2.load_pricedata(all_price_data)

    # execute the trades
    test_strategy.trade_loop()

    # implement sleep function here
    time.sleep(600)



