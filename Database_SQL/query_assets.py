from dotenv import load_dotenv
from Database_SQL.aws_sql_connect import AWS_SQL


# Connection
db_connection = AWS_SQL(load_dotenv)

def assets(connector,asset_config):
    urls_to_fetch = []
    for asset_id in asset_config:
        query =  f"SELECT live_data_url from {connector.DBNAME}.binance_assets WHERE id={asset_id}"
        connector.cursor.execute(query)
        table = connector.cursor.fetchall()
        urls_to_fetch.append({
                'url':table[0][0],
                'asset_id':asset_id
            })

    return urls_to_fetch