import random


class DumbStrategy:
    def __init__ (self):
        # (self, config_rows, connector_list)
        self.strategy_id = 1

    def execute_trading(self, config_rows):
        for obj in config_rows:
            # Preparation of trading relevant Data

            price_data = obj['pricedata'].fetch_price_data()
            # get latest trading account ballances
            account_cursor = obj['connector']
            account_info = account_cursor.get_account_info()
            trading_asset = obj['pricedata'].asset_dict
            ballance_trading_asset = account_cursor.get_ballance_of(trading_asset['ticker'])
            
            # Generation of signals 
            n = random.random()
            
            # Conditions to trade for Signal
            buy_condition = n >= 0.8
            sell_condition = n <= 0.2

            # Trading execution

            if (buy_condition == True):
                account_cursor.new_order(
                    'BUY',
                    'MARKET',
                    trading_asset['ticker'],
                    ballance_trading_asset/5
                )

            elif(sell_condition == False):
                account_cursor.new_order(
                    'SELL',
                    'MARKET',
                    trading_asset['ticker'],
                    ballance_trading_asset/5
                )
