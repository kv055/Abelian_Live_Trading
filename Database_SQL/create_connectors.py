import Strategies.find_parent as find_parent
from datetime import datetime
import requests
from dotenv import load_dotenv
from Database_SQL.aws_sql_connect import AWS_SQL, DummyData

connector = DummyData(load_dotenv)

# def connector_instance(key_pair):

#     pub = key_pair['pub_key']
#     priv = key_pair['priv_key']

#     if key_pair['data_provider'] == 'Binance':
#         connector_instance = BinanceSpot(pub, priv)
#         key_pair['connector'] = connector_instance
#         del key_pair['pub_key']
#         del key_pair['priv_key']
        
#     elif key_pair['data_provider'] == 'Alpaca':
#         connector_instance = Alpaca(pub, priv, 'https://broker-api.alpaca.markets/')
#         key_pair['connector'] = connector_instance
#         del key_pair['pub_key']
#         del key_pair['priv_key']
        
#     elif key_pair['data_provider'] == 'Kraken':
#         connector_instance = KrakenSpot(pub, priv)
#         key_pair['connector'] = connector_instance
#         del key_pair['pub_key']
#         del key_pair['priv_key']
    
def fetch_price_data(all_assets_to_fetch, connector=None):
    for asset in all_assets_to_fetch:
        # assign timestamp
        asset['last_fetched'] = datetime.now()

        if asset['data_provider'] == 'Binance':
            answer_raw = requests.get(asset['live_data_url'])
            answer_json = answer_raw.json()
            price_as_str = answer_json['price']
            price_as_float = float(price_as_str)
            asset['last_price'] = price_as_float

            
        elif asset['data_provider'] == 'Alpaca':
            asset['last_price'] = 69
            
        elif asset['data_provider'] == 'Kraken':
                      
            answer_raw = requests.get(asset['live_data_url'])
            answer_json = answer_raw.json()
            price_as_str = answer_json['result'][asset['ticker']]['o']
            price_as_float = float(price_as_str)
            asset['last_price'] = price_as_float
