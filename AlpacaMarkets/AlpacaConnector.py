import alpaca_trade_api as tradeapi

class Alpaca:
    def __init__(self, key, secr_key, select_api):
        self.alpaca_url = select_api
        self.pub_key = key
        self.priv_key = secr_key

        self.livetrading = tradeapi.REST(
            self.pub_key , 
            self.priv_key,
            self.alpaca_url
        )

    def get_account_info(self):
        return self.livetrading.get_account()

    def get_all_orders(self):
        # status=None, limit=None, after=None, until=None, direction=None, nested=None
        return self.livetrading.list_orders()

    def get_all_positions(self):
        return self.livetrading.list_positions()

    def get_history(self):
        # get_portfolio_history(date_start=None, date_end=None, period=None, timeframe=None, extended_hours=None)
        return self.livetrading.get_portfolio_history()

    def stop_all_orders(self):
        return self.livetrading.cancel_all_orders()

    def stop_order(self, id):
        return self.livetrading.cancel_order(id)

    def create_order(self):
        #  submit_order(symbol, 
        # qty=None, side="buy", type="market", time_in_force="day", 
        # limit_price=None, stop_price=None, client_order_id=None, 
        # order_class=None, take_profit=None, stop_loss=None, 
        # trail_price=None, trail_percent=None, notional=None)
        return self.livetrading.submit_order()


