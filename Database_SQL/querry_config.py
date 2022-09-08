from dotenv import load_dotenv
from Database_SQL.aws_sql_connect import AWS_SQL


# Connection
db_connection = AWS_SQL(load_dotenv)

class config_live_trading:
    def __init__(self, connector_instance):
        self.connector = connector_instance

    def Join(self):
        query =  f"""SELECT config_live_trading.id,config_live_trading.user_id, 
        exchange_keys.id,
        binance_assets.id,binance_assets.live_data_url,
        config_live_trading.strategy_id
        from {self.connector.DBNAME}.config_live_trading
        JOIN exchange_keys
        ON config_live_trading.user_id = exchange_keys.user_id
        JOIN binance_assets
        ON config_live_trading.asset_id = binance_assets.id
        """
        self.connector.cursor.execute(query)
        table = self.connector.cursor.fetchall()
        table_formated = []
        for row in table:
            row_as_dict = {
                'config_live_trading.id': row[0],
                'config_live_trading.user_id': row[1],
                'keys_id': row[2],
                'asset_id': row[3],
                'binance_assets.live_data_url': row[4],
                'strategy_id': row[5]
            }
            table_formated.append(row_as_dict)
        return table_formated
    
    # def query_config(self):
    #     query = f"SELECT * from {self.connector.DBNAME}.config_live_trading"
    #     self.connector.cursor.execute(query)
    #     config_table_contents = self.connector.cursor.fetchall()
    #     return config_table_contents

    def query_all_asset_id_from_config_rows(self):
        query = f"SELECT DISTINCT asset_id from {self.connector.DBNAME}.config_live_trading"
        self.connector.cursor.execute(query)
        config_table_contents = self.connector.cursor.fetchall()
        content = []
        for tuple in config_table_contents:
            content.append(tuple[0])
        return content

    def query_keys_id_DISTINCT(self):
        query = f"SELECT DISTINCT keys_id from {self.connector.DBNAME}.config_live_trading"
        self.connector.cursor.execute(query)
        config_table_contents = self.connector.cursor.fetchall()
        content = []
        for tuple in config_table_contents:
            content.append(tuple[0])
        return content
