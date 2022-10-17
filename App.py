import time

from Deployment.Deployment_Execution import Execute_Deployment
# from Message_Que.Test_File_Poll_Messages import Subscribe_Config_Rows
from Strategies.DummyStrategy import DumbStrategy

# Connecting to Q
# Q_Instance = Subscribe_Config_Rows()
Q_Instance = Execute_Deployment()

config_row_id_list = []
all_config_rows = []

asset_id_list = []
all_asset_url_dicts = []

key_id_list = []
all_connectors = []

test_strategy = DumbStrategy()

while True:

    Q_Instance.deploy_trading(
        config_row_id_list,
        all_config_rows,
        asset_id_list,
        all_asset_url_dicts,
        key_id_list,
        all_connectors
    )

    Q_Instance.stop_trading(
        all_config_rows,
        config_row_id_list
    )
    
    test_strategy.execute_trading(all_config_rows)

    time.sleep(1)