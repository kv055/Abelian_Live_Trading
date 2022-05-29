# # Binance
# from Binance.BinanceSpotClass import BinanceSpot
import random


class DumbStrategy:
    def __init__ (self, config_rows, connector_list):
        strategy_id = 1
        # filter all config rows that have a different Strategy id than the one  
        # in our current Strategy
        self.config = [row for row in config_rows if row['strategy_id'] == strategy_id]
        self.connector = connector_list

    def load_pricedata(self, price_data_list):
        # needs to be an INT
        self.price = price_data_list

    def trade(self):
        lol = self.connector.get_account_info()
        print(lol, self.price)

        n = random.random()
        if (n >= 0.75):
            print("RandomNumber >= 0.75: ", n, 'buy')
    # def __init__ (self, config):
    #     self.config = config
    #     pass

    # def trade(self, assets):
    #     # looking for intersections between assets.ticker and config.ticker
    #     for object in self.config:
    #         for element in assets:
    #             if object['ticker_symbol'] == assets['ticker_symbol']:
                    #do some shit
        # execute this method every 5min or so
        # lol = self.connector.get_account_info()
        # print(lol)
        # #     , ws, message
        # # print(message)
        # n = random.random()
        # if (n >= 0.75):
        #     print("RandomNumber >= 0.75: ", n, 'buy')
            
        #     # globalReturn['Action'].append({'type':'buy','positionSize': 0.5})
        #     # globalReturn['AssetValue'].append(self.price_raw[1][index_])
        #     # globalReturn['Time'].append(self.price_raw[0][index_])
        # elif(n <= 0.25):
        #     print("RandomNumber <= 0.25: ", n, 'sell')
            
        #     # globalReturn['Action'].append({'type':'sell','positionSize': 0.5})
        #     # globalReturn['AssetValue'].append(self.price_raw[1][index_])
        #     # globalReturn['Time'].append(self.price_raw[0][index_])

# Strategy must be a pure function, NO CLASS METHOD
# reaon being that it gets passed into the WebSockets module as callback
# doesnt wokr with a class method for whatever reason 

# def DumbStrategy(ws, message):
#     print(message)