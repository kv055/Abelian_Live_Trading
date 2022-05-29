import random


class DumbStrategy:
    def __init__ (self, config_rows, connector_list):
        strategy_id = 1
        # filter all config rows that have a different Strategy id than the one  
        # in our current Strategy
        self.config = [row for row in config_rows if row['strategy_id'] == strategy_id]
        self.connectors = connector_list

    def load_pricedata(self, price_data_list):
        self.price = price_data_list

    def trade_loop(self):
        for row in self.config:
            # get connecctor
            key_id = row['keys_id']
            connector_obj = [con for con in self.connectors if con['keys_id'] == key_id]

            # get asset price
            asset_id = row['asset_id']
            asset = [ass for ass in self.price if ass['asset_id'] == asset_id]
            
            # print('ROW',row,'ASSET',asset[0]['symbol'],'CONNECTOR',connector_obj)
            
            # if len(connector_obj) > 0:
            #     connection = connector_obj[0]['connector']
            #     account_info = connection.get_account_info()
            #     print(account_info)


    # def trade(self):
    #     lol = self.connectors.get_account_info()
    #     print(lol, self.price)

    #     n = random.random()
    #     if (n >= 0.75):
    #         print("RandomNumber >= 0.75: ", n, 'buy')