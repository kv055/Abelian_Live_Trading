import krakenex
# import krakenex.api as connector
from pykrakenapi import KrakenAPI

class KrakenSpot:
    def __init__(self, key, secr_key):
        self.pub_key = key
        self.priv_key = secr_key

        api = krakenex.API(self.pub_key, self.priv_key, 'https://futures.kraken.com/derivatives/api/v3')
        # api = connector(self.pub_key, self.priv_key)
        self.client = KrakenAPI(api)

    def get_account_info(self):
        ballance_as_frame = self.client.get_account_balance()
        self.ballance = dict(ballance_as_frame['vol'])
        return self.ballance

    def get_all_orders(self):
        pass

    def get_history(self):
        trade_history_as_frame = self.client.get_ledgers_info()
        print(trade_history_as_frame)

    def stop_all_orders(self):
        return 

    def stop_order(self, id):
        return 

    def create_order(self):
        return

# kilian = krakenex.API()
# kilian.load_key('kraken.key')

# balance = kilian.query_private('Balance')
# orders = kilian.query_private('OpenOrders')