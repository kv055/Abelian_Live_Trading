from dotenv import load_dotenv
from Database_SQL.aws_sql_connect import AWS_SQL


# Connection
db_connection = AWS_SQL(load_dotenv)

class config_live_trading:
    def __init__(self, connector_instance):
        self.connector = connector_instance        

    def query_all_asset_id_from_config_rows(self):
        query = f"""
            SELECT DISTINCT 
                config_live_trading.asset_id,
                assets.data_provider,
                assets.ticker,
                assets.live_data_url,
                assets.live_data_req_body
            FROM config_live_trading
            WHERE status_active = '0'
            JOIN assets
                ON config_live_trading.asset_id = assets.id
        """
        self.connector.cursor.execute(query)
        config_table_contents = self.connector.cursor.fetchall()
        return config_table_contents

    def query_keys_id_DISTINCT(self):
        query = f"""
            SELECT DISTINCT keys_id from config_live_trading
            WHERE status_active = '0'
        """
        self.connector.cursor.execute(query)
        config_table_contents = self.connector.cursor.fetchall()

        return config_table_contents
