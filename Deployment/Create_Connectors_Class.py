import json
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
            latest_closing_price = latest_bar._raw['c']
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

    def get_ballance_of_trading_asset_and_cash(self, asset_dict):
        if self.endpoint == 'Alpaca':
            # Get Asset Ballances
            answer = self.client.list_positions()
            list_of_positions = [pos._raw for pos in answer]
            def filter_function(position_from_alpaca):
                if position_from_alpaca['symbol'] == asset_dict['ticker']:
                    return True
                    # Asset Dict Append Ballance
                else:
                    return False
            filter_object = filter(filter_function, list_of_positions)
            list_of_position_with_ballance_of_speccified_asset = list(filter_object)

            # Get Cash Ballances
            account = self.client.get_account()
            cash = account._raw['cash']

            if len(list_of_position_with_ballance_of_speccified_asset) == 0:
                return {                     
                    'Asset_Ballance': 0,
                    'Cash_Ballance': cash
                    }
            else:
                return {
                    'Asset_Ballance': list_of_position_with_ballance_of_speccified_asset[0]['qty'],
                    'Cash_Ballance': cash
                }

            

            # formated_positions = []
            # for position in list_of_positions:
            #     formated_positions.append(
            #         {
                        
            #         }
            #     )

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
            activities = self.client.get_activities()
            

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
    
    def new_order(self,order_dict):
        if self.endpoint == 'Alpaca':
            generated_order = self.client.submit_order(
                order_dict['ticker'],
                order_dict['quantity'],
                order_dict['side'],
                order_dict['type'],
                order_dict['time_in_force']
            )

            return generated_order
            
        # submit_order(symbol, 
        # qty=None, side="buy", type="market", time_in_force="day", 
        # limit_price=None, stop_price=None, client_order_id=None, 
        # order_class=None, take_profit=None, stop_loss=None, 
        # trail_price=None, trail_percent=None, notional=None)
            

        elif self.endpoint == 'Binance':
            generated_order = self.client.cancel_order(id)
            

        elif self.endpoint == 'Kraken':
            # generated_order = self.client.
            pass

        # success = True
        # if success == True:
        #     return 0
        # else:
        #     return 1
        
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


