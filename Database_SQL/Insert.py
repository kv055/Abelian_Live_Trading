from dotenv import load_dotenv
from aws_sql_connect import AWS_SQL


# Connection
db_connection = AWS_SQL(load_dotenv)

asset = {
    'asset_name': 'BitchCoin'
}

def insert_assets(connector, asset_dict):
    # ins = f"""INSERT INTO config_live_trading (user_id, strategy_id,asset_id) VALUES (%s,%s,%s)"""
    # val = (asset['asset_name'])
    # connector.cursor.execute(ins,val)
    # connector.connection.commit()
    pass

insert_assets()