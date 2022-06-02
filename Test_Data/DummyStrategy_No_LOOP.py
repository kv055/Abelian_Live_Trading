import random

class DumbStrategy:
    def __init__ (self, config_rows, connector_list):
        strategy_id = 1
        # filter all config rows that have a different Strategy id than the one  
        # in our current Strategy
        self.config = config_rows
        self.connectors = connector_list

    def load_pricedata(self, price_data_list):
        self.price = price_data_list

    def trade_loop(self):
        n = random.random()
        if (n >= 0.5):
            print("RandomNumber >= 0.75: ", n, 'buy')
            # info = self.connectors.get_account_info()

            # this needs to be universaly accepted by every connector class
            order = {
                'side': 'buy',
                'ticker':'TSLA',
                'order_type': 'market',
                'quantity': 20,
                'time_in_force': 'gtc'
            }
            buy = self.connectors.market_order(order)
            print(buy)
        elif (n <= 0.5):
            print("RandomNumber >= 0.75: ", n, 'sell')
            # info = self.connectors.get_account_info()
            
            # this needs to be universaly accepted by every connector class
            order = {
                'side': 'sell',
                'ticker':'TSLA',
                'order_type': 'market',
                'quantity': 20,
                'time_in_force': 'gtc'
            }
            sell = self.connectors.market_order(order)
            print(sell)
            