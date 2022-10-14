from datetime import datetime
import requests
    
class Create_Price_Refresh:
    def __init__(self, asset_dict, connector):
        self.asset_dict = asset_dict
        self.endpoint = asset_dict['data_provider']
        self.connector = connector

    def fetch_price_data(self):
        # self.asset_dict['last_fetched'] = datetime.now()
        self.last_fetched = datetime.now()

        if self.endpoint == 'Binance':
            answer_raw = requests.get(self.asset_dict['live_data_url'])
            answer_json = answer_raw.json()
            price_as_str = answer_json['price']
            price_as_float = float(price_as_str)
                        
        elif self.endpoint == 'Alpaca':
            price_as_float = self.connector.get_latest_pricedata(self.asset_dict['ticker'])
            
        elif self.endpoint == 'Kraken':        
            answer_raw = requests.get(self.asset_dict['live_data_url'])
            answer_json = answer_raw.json()
            price_as_str = answer_json['result'][self.asset_dict['ticker']]['o']
            price_as_float = float(price_as_str)
            
        return {
            'data_provider': self.endpoint,
            'ticker': self.asset_dict['ticker'],
            'last_fetched': self.last_fetched,
            'last_price': price_as_float
        } 