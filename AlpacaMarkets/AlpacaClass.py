import alpaca_trade_api as tradeapi

# Endpoints
APCA_API_BASE_URL =	'https://api.alpaca.markets' 
APCA_API_DATA_URL = 'https://data.alpaca.markets'
APCA_API_PAPERTRADING_URL = 'https://paper-api.alpaca.markets'

# Keys
PAPER_APCA_API_KEY_ID = 'PK0RPI7F5X8M0VVED26I'
PAPER_APCA_API_SECRET_KEY = '6VoDwGzKZ3uvPPq8awfspLesuYDnPqYtx0ZhPefG'

APCA_API_KEY_ID = 'AKTY9EUCRJZWTAIQVKQR'
APCA_API_SECRET_KEY = 'Beynq6kJ4aCapM3E6xRH5BDhziFzuMaxyCTjMwIq'


class Alpaca:
    def __init__(self, key, secr_key, select_api):
        self.alpaca_url = select_api
        self.pub_key = key
        self.priv_key = secr_key

        self.livetrading = tradeapi.REST(
            APCA_API_KEY_ID, 
            APCA_API_SECRET_KEY,
            APCA_API_BASE_URL
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


