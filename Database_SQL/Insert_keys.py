from dotenv import load_dotenv
from aws_sql_connect import AWS_SQL


# Connection
db_connection = AWS_SQL(load_dotenv)

keys = {
    'user_id': 69,
    'exchange_id': 69,
    'exchange_name': 69,
    'pub_key': 420,
    'priv_key': 420
}

def insert_exchange_keys(connector, keys_dict):
    ins = f"""INSERT INTO exchange_keys 
    (user_id, exchange_id,exchange_name,pub_key,priv_key) VALUES (%s,%s,%s,%s,%s)"""
    val = (keys['user_id'],keys['exchange_id'],keys['exchange_name'],keys['pub_key'],keys['priv_key'])
    connector.cursor.execute(ins,val)
    connector.connection.commit()


insert_exchange_keys(db_connection, keys)