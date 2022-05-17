import find_parent
from Database_SQL.query_keys import keys

from dotenv import load_dotenv
from Database_SQL.aws_sql_connect import AWS_SQL, DummyData

#Querry DB
from Database_SQL.query_keys import keys
from Database_SQL.querry_config import config_live_trading

# import exchange connectors
from Binance.BinanceSpotConnector import BinanceSpot
from AlpacaMarkets.AlpacaConnector import Alpaca

# Connection
connector = DummyData(load_dotenv)

def connector_instances():
   # querry all DISTINCT KEYS
    query = config_live_trading(connector)
    key_ids = query.query_keys_id_DISTINCT()
    list_of_keys = keys(connector, key_ids)

    for key_pair in list_of_keys:
        pub = key_pair['pub_key']
        priv = key_pair['priv_key']
        if key_pair['endpoint'] == 'Binance':
            connector_instance = BinanceSpot(pub, priv)
            key_pair['connector'] = connector_instance
            del key_pair['pub_key']
            del key_pair['priv_key']
            
        elif key_pair['endpoint'] == 'Alpaca':
            connector_instance = Alpaca(pub, priv, 'https://broker-api.alpaca.markets/')
            key_pair['connector'] = connector_instance
            del key_pair['pub_key']
            del key_pair['priv_key']
            
    return list_of_keys

        
# class create_connectors:
#     def __init__(self, connector, keys_config):
        
#         pass

    