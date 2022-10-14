import random

class DumbStrategy:
    def __init__ (self):
        # (self, config_rows, connector_list)
        self.strategy_id = 1

    def execute_trading(self, config_rows):
        for obj in config_rows:
            # get latest price
            price_data = obj['pricedata'].fetch_price_data()
            # get latest trading account ballances
            account_cursor = obj['connector']
            account_info = account_cursor.get_account_info()
            trading_asset = obj['pricedata']['asset_dict']
            ballance_trading_asset = account_cursor.get_ballance_of(trading_asset)
            n = random.random()
            # if (n >= 0.8):
            #     account_cursor.new_order('BTCUSDT','BUY','MARKET',0.002)
            # elif(n <= 0.2):
            #     account_cursor.new_order('BTCUSDT','SELL','MARKET',0.002)