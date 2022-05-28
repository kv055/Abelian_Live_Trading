import find_parent
from Database_SQL.query_assets import assets
from Database_SQL.querry_config import config_live_trading
from dotenv import load_dotenv
import requests

# Import Database Connection
from Database_SQL.aws_sql_connect import AWS_SQL, DummyData
# connection = AWS_SQL(load_dotenv)
connector = DummyData(load_dotenv)


def live_price_data_Binance():
    # query asset_ids from Config
    query = config_live_trading(connector)
    asset_ids = query.query_asset_id_DISTINCT()

    urls_to_fetch = assets(connector, asset_ids)
    
    price_data = []
    for row in urls_to_fetch:
        answer_raw = requests.get(row['url'])
        answer_json = answer_raw.json()
        answer_json['asset_id'] = row['asset_id']
        price_data.append(answer_json)

    return price_data


# live_price_data_Binance()