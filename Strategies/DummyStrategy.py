# # Binance
# from Binance.BinanceSpotClass import BinanceSpot
import random


class DumbStrategy:
    def __init__ (self, connector):
        self.connector = connector
        

    def load_pricedata(self,pricedata):
        # needs to be an INT
        self.price = pricedata

    def trade(self):
        lol = self.connector.get_account_info()
        print(lol, self.price)

        n = random.random()
        if (n >= 0.75):
            print("RandomNumber >= 0.75: ", n, 'buy')
            
        #     # globalReturn['Action'].append({'type':'buy','positionSize': 0.5})
        #     # globalReturn['AssetValue'].append(self.price_raw[1][index_])
        #     # globalReturn['Time'].append(self.price_raw[0][index_])
        elif(n <= 0.25):
            print("RandomNumber <= 0.25: ", n, 'sell')
            
        #     # globalReturn['Action'].append({'type':'sell','positionSize': 0.5})
        #     # globalReturn['AssetValue'].append(self.price_raw[1][index_])
        #     # globalReturn['Time'].append(self.price_raw[0][index_])

# Strategy must be a pure function, NO CLASS METHOD
# reaon being that it gets passed into the WebSockets module as callback
# doesnt wokr with a class method for whatever reason 

# def DumbStrategy(ws, message):
#     print(message)