import os
from Deployment.Create_Connectors_Class import Create_Connectors
from Deployment.Create_Asset_Dicts_Class import Create_Price_Refresh
from Strategies.DummyStrategy import DumbStrategy

def initialize_strategy():
    # Get Priv Keys
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
    asset_dict = {
        "data_provider": "Binance",
        "ticker": "BTCUSDC",
        "candleSize": "1_Hour",
        "live_data_url": f'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDC'
    }

    # INITIALIZE CONNECTOR OBJECT
    connector = Create_Connectors(keys_dict)

    # INITIALIZE PRICE DATA OBJECT
    price_data = Create_Price_Refresh(asset_dict, connector)

    # CREATE TRADING OBJECT
    trading_obj = {
        'pricedata': price_data.fetch_price_data,
        'connector': connector,
        'asset_dict': asset_dict
    }

    # INITIALIZE STRATEGY
    all_config_rows = []
    test_strategy = DumbStrategy()

    # Add the trading object to the strategy
    test_strategy.add_trading_object(trading_obj)

    return test_strategy, all_config_rows
