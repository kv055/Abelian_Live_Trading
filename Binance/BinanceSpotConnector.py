from binance.spot import Spot


class BinanceSpot:
    def __init__(self, key, secr_key):
        # ,select_api
        # self.alpaca_url = select_api
        self.pub_key = key
        self.priv_key = secr_key
        self.client = Spot(self.pub_key, self.priv_key)
        # TestNet Client
        # self.client = Spot(self.pub_key, self.priv_key, {"base_url": 'https://testnet.binance.vision/api'})
        # self.client = Spot(self.pub_key, self.priv_key, base_url = 'https://testnet.binance.vision/api')


    def get_account_info(self):
        return self.client.account()

    def get_all_orders(self):
        # status=None, limit=None, after=None, until=None, direction=None, nested=None
        return self.client.get_open_orders()

    # def get_all_positions(self):
    #     return self.client.list_positions()

    def get_history(self):
        # get_portfolio_history(date_start=None, date_end=None, period=None, timeframe=None, extended_hours=None)
        return self.client.my_trades()

    def stop_all_orders(self):
        return self.client.cancel_open_orders()

    def stop_order(self, id):
        return self.client.cancel_order(id)

    def create_order(self):
        # params = {
        #     'symbol': 'BTCUSDT',
        #     'side': 'SELL',
        #     'type': 'LIMIT',
        #     'timeInForce': 'GTC',
        #     'quantity': 0.002,
        #     'price': 9500
        # }
        return self.client.new_order()



