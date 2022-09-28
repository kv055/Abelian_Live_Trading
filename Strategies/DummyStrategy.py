import random

class DumbStrategy:
    def __init__ (self):
        # (self, config_rows, connector_list)
        self.strategy_id = 1
        # # filter all config rows that have a different Strategy id than the one  
        # # in our current Strategy
        # self.config = [row for row in config_rows if row['strategy_id'] == self.strategy_id]
        # self.connectors = connector_list

    def init_trade_objects(self, config_rows, price_data_list,connector_list):
        self.config = [row for row in config_rows if row['strategy_id'] == self.strategy_id]
        self.all_assets_pricedata = price_data_list
        self.connectors = connector_list
        self.trade_objects = []
        for row in self.config:
            # get connecctor
            key_id = row['keys_id']
            connector_obj = [con for con in self.connectors if con['keys_id'] == key_id]
            account = connector_obj[0]['connector']
            # get asset price
            asset_id = row['asset_id']
            asset = [ass for ass in self.all_assets_pricedata if ass['id'] == asset_id]
       
            self.trade_objects.append({
                'Account': account,
                'Asset': asset[0],
                'Config': row
            })

    def execute_trading(self):
        for object in self.trade_objects:
            account_cursor = object['Account']
            account_info = account_cursor.get_account_info()
            n = random.random()
            if (n >= 0.8):
                account_cursor.new_order('BTCUSDT','BUY','MARKET',0.002)
            elif(n <= 0.2):
                account_cursor.new_order('BTCUSDT','SELL','MARKET',0.002)