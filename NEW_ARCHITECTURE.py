from dotenv import load_dotenv
import time

from Message_Que.Test_File_Poll_Messages import Subscribe_Config_Rows
from Database_SQL.aws_sql_connect import DummyData
from Database_SQL.create_connectors import fetch_price_data
# Import Strategies
from Strategies.DummyStrategy import DumbStrategy


# Conecting to DB
connection = DummyData(load_dotenv)

# Connecting to Q
Q_Instance = Subscribe_Config_Rows()

all_config_rows = []

asset_id_list = []
all_asset_url_dicts = []

key_id_list = []
all_connectors = []

test_strategy = DumbStrategy()

while True:
    # fetch config rows from Q
    config_rows_from_Q = Q_Instance.fetch_deploy_messages()
    Q_Instance.deploy_config_rows(
        config_rows_from_Q,
        all_config_rows,
        asset_id_list,
        all_asset_url_dicts,
        key_id_list,
        all_connectors
    )
    

    stop_trading_messages = Q_Instance.fetch_stop_trading_messages(all_config_rows)

    # fetch all pricedata from all_asset_url_dicts
    fetch_price_data(all_asset_url_dicts)

    test_strategy.init_trade_objects(
        all_config_rows, 
        all_asset_url_dicts, 
        all_connectors)
    
    # test_strategy.execute_trading()

    time.sleep(10)