import random

class DumbStrategy:
    def __init__ (self, config_rows, connector_list):
        strategy_id = 1
        # filter all config rows that have a different Strategy id than the one  
        # in our current Strategy
        self.config = 0
        self.connectors = 0

    def load_pricedata(self, price_data_list):
        self.price = price_data_list

    def trade_loop(self):
        n = random.random()
        if (n >= 0.5):
            print("RandomNumber >= 0.75: ", n, 'buy')
        elif (n <= 0.5):
            print("RandomNumber >= 0.75: ", n, 'sell')