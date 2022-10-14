# put the logic of Test File Poll messages in here
# minus the part where the messages get polled

# if it works then delete functions x y from Poll_Messages.py

from Database_SQL.Querry_Config_Class import config_live_trading
from Deployment.Create_Connectors_Class import Create_Connectors
from Deployment.Create_Asset_Dicts_Class import Create_Price_Refresh

from Message_Que.Poll_Messages_Class import Subscribe_Config_Rows

class Execute_Deployment:
    def __init__(self):
        self.que_subscription = Subscribe_Config_Rows()
        self.config_table = config_live_trading() 

    def stop_trading(
        self, 
        all_config_rows, 
        list_of_deployed_config_row_ids
        ):
        
        fetched_messages = self.que_subscription.fetch_stop_trading_messages()
        # if fetched_messages == True:
        for message in fetched_messages:
            # filter function
            def find_deployed_config_by_id(deployed_strategy):
                if deployed_strategy['id'] == message['Config_row_Id']:
                    return True
            
            def find_deployed_id(deployed_config_row_id):
                if deployed_config_row_id == message['Config_row_Id']:
                    return True

            matched_deployed_configuration =  list(
                filter(
                find_deployed_config_by_id,
                all_config_rows
            ))

            matched_deployed_id =  list(
                filter(
                find_deployed_id,
                list_of_deployed_config_row_ids
            ))

            for config_row in matched_deployed_configuration:
                all_config_rows.remove(config_row)

            for id in matched_deployed_id:
                list_of_deployed_config_row_ids.remove(id)
            
            # delete message id from row in the DB
            self.config_table.delete_message_id_from_stoped_config_rows(message['Config_row_Id'])

            # To do: delete message from Q delete message from Q

    def deploy_trading(
        self,
        config_row_id_list,
        deployed_config_rows,
        asset_id_list,
        deployed_assets,
        key_id_list,
        deployed_connectors
        ):

        fetched_messages = self.que_subscription.fetch_deploy_trading_messages()
        # if fetched_messages == True:
        for message in fetched_messages:
            config_row = message['Config_Row']

            if config_row['id'] not in config_row_id_list:
                config_row_id_list.append(config_row['id'])

                asset_id = config_row['asset_id']
                keys_id = config_row['keys_id']

                if keys_id not in key_id_list:

                    key_pair = self.config_table.get_key_pair_by_id(keys_id)
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
                
                elif keys_id in key_id_list:
                    # filter connector by key_id
                    connector_filtered = [con for con in deployed_connectors if con['keys_id'] == keys_id]
                    connector = connector_filtered[0]

                if asset_id not in asset_id_list:
                    
                    asset_dict = self.config_table.get_asset_by_id(asset_id)
                    # Create asset dict
                    price_data_instance = Create_Price_Refresh(asset_dict[0],connector)
            
                    deployed_assets.append(price_data_instance)
                    asset_id_list.append(asset_id)

                elif asset_id in asset_id_list:
                    # filter by deployed assets
                    price_data_instance_filtered = [ass for ass in deployed_assets if ass['id'] == asset_id]
                    price_data_instance = price_data_instance_filtered[0]


                config_row['pricedata'] = price_data_instance
                config_row['connector'] = connector

                deployed_config_rows.append(config_row)