import alpaca_trade_api as tradeapi

class Alpaca:
    # all possible endpoints
    # 'https://api.alpaca.markets/'
    # 'https://paper-api.alpaca.markets'

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

    def market_order(self, order_dict):
        oder_side = order_dict['side']
        order_symbol = order_dict['ticker']
        order_type = order_dict['order_type']
        order_qty = order_dict['quantity']
        time_in_force = order_dict['time_in_force']

        return self.livetrading.submit_order(
                side= oder_side,
                symbol= order_symbol,
                type= order_type,
                qty= order_qty,
                time_in_force= time_in_force
        )

    def limit_order(self):
        return self.livetrading.submit_order(
                side= "buy",
                symbol= "TSLA",
                type= "limit",
                qty= "10",
                time_in_force= "gtc",
                limit_price= 420
        )

    def stop_order(self):
        return self.livetrading.submit_order(
                side= "buy",
                symbol= "TSLA",
                type= "stop",
                qty= "10",
                time_in_force= "gtc",
                stop_price= 420
        )

    def stop_limit_order(self):
        return self.livetrading.submit_order(
                side= "buy",
                symbol= "TSLA",
                type= "stop_limit",
                qty= "10",
                time_in_force= "gtc",
                limit_price= 420,
                stop_price=300
        )

    def trailing_stop_order(self):
        return self.livetrading.submit_order(
                side= "buy",
                symbol= "TSLA",
                type= "market",
                qty= "10",
                time_in_force= "gtc"
        )


            #     'symbol':'TSLA', 
            #     'qty':1, 
            #     'side':"buy",
            #     'type':"market",
            #     'time_in_force':"day" 
            #     # limit_price=None, stop_price=None, client_order_id=None, 
            #     # order_class=None, take_profit=None, stop_loss=None, 
            #     # trail_price=None, trail_percent=None, notional=None)
            # }

    # for DB-maintenance

    def get_assets(self):
        return self.livetrading.get('/assets')

    def get_historical(self):
        symbol = 'TSLA'
        params = {}
        params['timeframe'] = '59Min'
        return self.livetrading.get(f'/stocks/{symbol}/bars', params)

    def get_live_data(self):
        symbol = 'TSLA'
        return self.livetrading.get(f'/stocks/{symbol}/bars/latest')
    