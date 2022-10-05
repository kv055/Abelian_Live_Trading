from dotenv import load_dotenv
import time

from Message_Que.Test_File_Poll_Messages import Subscribe_Config_Rows
from Database_SQL.aws_sql_connect import DummyData
# Import Strategies
from Strategies.DummyStrategy import DumbStrategy


# Conecting to DB
connection = DummyData(load_dotenv)

# Connecting to Q
Q_Instance = Subscribe_Config_Rows()

config_row_id_list = []
all_config_rows = []

asset_id_list = []
all_asset_url_dicts = []

key_id_list = []
all_connectors = []

test_strategy = DumbStrategy()

while True:

    Q_Instance.deploy_config_rows(
        config_row_id_list,
        all_config_rows,
        asset_id_list,
        all_asset_url_dicts,
        key_id_list,
        all_connectors
    )

    Q_Instance.stop_trading_messages(all_config_rows)
    
    test_strategy.execute_trading(all_config_rows)

    time.sleep(1)