from dotenv import load_dotenv
from aws_sql_connect import AWS_SQL


# Connection
db_connection = AWS_SQL(load_dotenv)

config = {
    'user_id': 7,
    'strategy_id': 1,
    'asset_id': 69
}

def insert_config(connector, config_dict):
    ins = f"""INSERT INTO config_live_trading (user_id, strategy_id,asset_id) VALUES (%s,%s,%s)"""
    val = (config['user_id'],config['strategy_id'],config['asset_id'])
    connector.cursor.execute(ins,val)
    connector.connection.commit()


insert_config(db_connection, config)
