import os
import load_dotenv

from Deployment.Create_Connectors_Class import Create_Connectors
from Deployment.Create_Asset_Dicts_Class import Create_Price_Refresh
from Strategies.DummyStrategy import DumbStrategy

# INITIALIZE STRATEGY
all_config_rows = []
test_strategy = DumbStrategy()

# Get Priv Keys
load_dotenv()
pub_key = os.getenv('BINANCE_PUB')
priv_key = os.getenv('BINANCE_PRIV')
api_endpoint = os.getenv('BINANCE_API_END')

keys_dict = {
    # BINANCE KEYS
    'data_provider': 'Binance',
    'pub_key': pub_key,
    'priv_key': priv_key,
    'api_endpoint': api_endpoint
}
asseet_dict = {
    "data_provider": "Binance",
    "ticker": "BTCUSDC",
    "candleSize": "1_Hour"
}

# INITIALIZE CONNECTOR OBJECT
connector = Create_Connectors(keys_dict)

# INITIALIZE PRICE DATA OBJECT
price_data = Create_Price_Refresh(asseet_dict, connector)

# CREATE TRADING OBJECT
obj = {
    'pricedata': price_data.fetch_price_data,
    'connector': connector,
    'asset_dict': asseet_dict
}
all_config_rows.append(obj)


def lambda_handler(event, context):
    test_strategy.execute_trading(all_config_rows)
    return {
        'statusCode': 200,
        'body': 'Execution completed'
    }
