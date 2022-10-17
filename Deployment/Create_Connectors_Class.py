import alpaca_trade_api as tradeapi
import krakenex
from binance.spot import Spot
from pykrakenapi import KrakenAPI


class Create_Connectors:
    def __init__(self, key_dict):
        self.endpoint = key_dict['data_provider']
        
        if self.endpoint == 'Alpaca':
            self.client = tradeapi.REST(
                key_dict['pub_key'], 
                key_dict['priv_key'], 
                key_dict['api_endpoint']
            )
                        
        elif self.endpoint == 'Binance':
            self.client = Spot(
                key_dict['pub_key'], 
                key_dict['priv_key']
            )

        elif self.endpoint == 'Kraken':
            api = krakenex.API(
                key_dict['pub_key'], 
                key_dict['priv_key'], 
                key_dict['api_endpoint']
            )
            self.client = KrakenAPI(api)
    
    # Public Market Data
    def get_latest_pricedata(self, ticker):
        if self.endpoint == 'Alpaca':
            latest_bar = self.client.get_latest_bar(ticker)
            latest_closing_price = latest_bar['c']
        
            return latest_closing_price

    # Private Trading 

    def get_account_info(self):
        if self.endpoint == 'Alpaca':
            account = self.client.get_account()
            

        elif self.endpoint == 'Binance':
            account = self.client.account()
            

        elif self.endpoint == 'Kraken':
            ballance_as_frame = self.client.get_account_balance()
            ballance = dict(ballance_as_frame['vol'])
            account = 6999
            
        return account

    def get_ballance_of(self, ticker):
        if self.endpoint == 'Alpaca':
            account = self.client.get_account()
            
            

        elif self.endpoint == 'Binance':
            account = self.client.account()
            

        elif self.endpoint == 'Kraken':
            ballance_as_frame = self.client.get_account_balance()
            ballance = dict(ballance_as_frame['vol'])
            account = 6999


    def get_all_orders(self):
        if self.endpoint == 'Alpaca':
            # status=None, limit=None, after=None, until=None, direction=None, nested=None
            open_orders = self.client.list_orders()
            

        elif self.endpoint == 'Binance':
            # status=None, limit=None, after=None, until=None, direction=None, nested=None
            open_orders = self.client.get_open_orders()
            

        elif self.endpoint == 'Kraken':
            # open_orders = self.client.
            pass


    def get_history(self, ticker_symbol=None):
        if self.endpoint == 'Alpaca':
           history = self.client.get_portfolio_history()
            

        elif self.endpoint == 'Binance':
            history = self.client.my_trades(ticker_symbol)
            

        elif self.endpoint == 'Kraken':
            history = self.client.get_ledgers_info()
            


    def stop_all_orders(self, ticker_symbol=None):
        if self.endpoint == 'Alpaca':
            stopped_orders = self.client.cancel_all_orders()
            

        elif self.endpoint == 'Binance':
            stopped_orders = self.client.cancel_open_orders(ticker_symbol)

        elif self.endpoint == 'Kraken':
            # stopped_orders = self.client.
            pass


    def stop_order(self, id):
        if self.endpoint == 'Alpaca':
            stopped_order = self.client.cancel_order(id)
            

        elif self.endpoint == 'Binance':
            stopped_order = self.client.cancel_order(id)
            

        elif self.endpoint == 'Kraken':
            # stopped_order = self.client.
            pass

        # Binance
        # params = {
        #     'symbol': 'BTCUSDT',
        #     'side': 'SELL',
        #     'type': 'MARKET',
        #     'timeInForce': 'GTC',
        #     'quantity': 0.002,
        #     # 'price': 9500
        # }
        # 'BTCUSDT','BUY','MARKET',0.002

        # Alpaca
        #  submit_order(symbol, 
        # qty=None, side="buy", type="market", time_in_force="day", 
        # limit_price=None, stop_price=None, client_order_id=None, 
        # order_class=None, take_profit=None, stop_loss=None, 
        # trail_price=None, trail_percent=None, notional=None)

