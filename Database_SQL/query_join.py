
import find_parent
# from dotenv import load_dotenv

# # Import Database Connection
# from Database_SQL.aws_sql_connect import AWS_SQL

# # Conecting to DB
# connection = AWS_SQL(load_dotenv)

def Join(connector):
    query =  f"""SELECT config_live_trading.user_id, 
    exchange_keys.pub_key,exchange_keys.priv_key,
    binance_assets.live_data_url,
    config_live_trading.strategy_id
    from {connector.DBNAME}.config_live_trading
    JOIN exchange_keys
    ON config_live_trading.user_id = exchange_keys.user_id
    JOIN binance_assets
    ON config_live_trading.asset_id = binance_assets.id
    """
    connector.cursor.execute(query)
    table = connector.cursor.fetchall()
    l = 0

# Join(connection)



# query =  f"""SELECT config_live_trading.user_id, exchange_keys.pub_key,exchange_keys.priv_key 
#     from {connector.DBNAME}.config_live_trading
#     INNER JOIN exchange_keys
#     ON config_live_trading.user_id = exchange_keys.user_id
#     """