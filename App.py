from dotenv import load_dotenv
import time
import requests
load_dotenv()

# Import Database Connection
from Database_SQL.aws_sql_connect import AWS_SQL, DummyData
from Database_SQL.Querry_Config_Class import config_live_trading 

# Import live data fetch modules
# from Binance.FetchLiveData import live_price_data_Binance
# Import connections
from Database_SQL.create_connectors import connector_instances
# Import Strategies
from Strategies.DummyStrategy import DumbStrategy
from Message_Que.Test_File_Poll_Messages import Subscribe_Config_Rows

# Conecting to DB
connection = DummyData(load_dotenv)

# Connecting to Q
Q_Instance = Subscribe_Config_Rows()
# fetch config rows from Q
Q_Instance.fetch_config_rows_from_Q()

# Fetch all assets from Config module
querry_from = config_live_trading(connection)
config_rows_DB = querry_from.Join()

# create exchange/broker connections from config rows
connectors = connector_instances()

# all price data urls


# Init all Strategies
test_strategy = DumbStrategy(config_rows_DB, connectors)

while True:


    # fetch price_Data
    # all_price_data = live_price_data_Binance()
    
    # feed pricedata to Strategies
    test_strategy.load_pricedata()

    # execute the trades
    test_strategy.trade_loop()

    # implement sleep function here
    time.sleep(600)