import time
from dotenv import load_dotenv

from Message_Que.Q_PUB_SUB_class import Q
from Database_SQL.aws_sql_connect import DummyData
from Broker_Exchange_Connectors.Create_Connectors_Class import Create_Connectors

class Subscribe_Config_Rows:
    def __init__(self):
        self.que = Q()
        self.db_instance = DummyData(load_dotenv)
        self.deployed_strategies = []


    def fetch_deploy_messages(self):
        fetched_messages = self.que.subscribe()

        for message in fetched_messages:
            if len(message) > 0:
                if message['Message_Group'] == 'Deploy' and message not in self.deployed_strategies:
                    self.deployed_strategies.append(message)
        # To do: delete message from Q

        return self.deployed_strategies
        

    def fetch_stop_trading_messages(self, all_config_rows):
        fetched_messages = self.que.subscribe()

        for message in fetched_messages:
            if message['Message_Group'] == 'Stop_Trading':
                # filter function
                def find_deployed_config_by_id(deployed_strategy):
                    if deployed_strategy['id'] == message['Config_row_Id']:
                        return True
                # find the deployed strat by the messageid from the stop message 
                matched_deployed_configuration =  list(
                    filter(
                    find_deployed_config_by_id,
                    all_config_rows
                ))
                for config_row in matched_deployed_configuration:
                    all_config_rows.remove(config_row)
                # delete message id from row in the DB
                update_row_sql = f"""
                    UPDATE config_live_trading
                    SET message_id = 'NULL'
                    WHERE id = '{message['Config_row_Id']}' 
                """
                self.db_instance.cursor.execute(update_row_sql)
                self.db_instance.connection.commit()

                # # To do: delete message from Q delete message from Q

    def deploy_config_rows(
        self,
        new_config_rows_to_deploy,
        deployed_config_rows,
        asset_id_list,
        deployed_assets,
        key_id_list,
        deployed_connectors
        ):

        if len(new_config_rows_to_deploy) > 0:
            for message in new_config_rows_to_deploy:
                
                asset_id = message['Config_Row']['asset_id']
                keys_id = message['Config_Row']['keys_id']
                
                if message['Config_Row'] not in deployed_config_rows:
                    deployed_config_rows.append(message['Config_Row']) 

                if asset_id not in asset_id_list:
                    
                    get_asset_data_sql = f"""
                        SELECT
                            assets.id,
                            assets.data_provider, 
                            assets.ticker, 
                            assets.live_data_url,
                            assets.live_data_req_body
                        FROM assets
                        WHERE assets.id = '{asset_id}'

                    """
                    self.db_instance.cursor.execute(get_asset_data_sql)
                    asset_dicts_unformated = self.db_instance.cursor.fetchall()
                    
                    for asset in asset_dicts_unformated:
                        deployed_assets.append(asset)

                    asset_id_list.append(asset_id)

                if keys_id not in key_id_list:

                    get_key_pair_sql = f"""
                        SELECT
                            exchange_keys.data_provider,
                            exchange_keys.api_endpoint,
                            exchange_keys.pub_key,
                            exchange_keys.priv_key
                        FROM exchange_keys
                        WHERE exchange_keys.id = '{keys_id}'

                    """
                    self.db_instance.cursor.execute(get_key_pair_sql)
                    key_pair = self.db_instance.cursor.fetchall()

                    key_pair[0]['keys_id'] =  keys_id
                    # make connector out of it
                    # connector_instance(key_pair[0])
                    connector = Create_Connectors(key_pair[0])
                    # append connector to all_connetors

                    deployed_connectors.append({
                        'keys_id' : keys_id,
                        'connector' : connector
                    })
                    key_id_list.append(keys_id)