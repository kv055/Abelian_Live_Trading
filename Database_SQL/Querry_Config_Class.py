from Database_SQL.aws_sql_connect import SQL_Server


class config_live_trading:
    def __init__(self):
        self.connector = SQL_Server('DummyData')        

    def cursor_fetch(self, sql_querry_string):
        self.connector.cursor.execute(sql_querry_string)
        sql_output = self.connector.cursor.fetchall()
        return sql_output

    def query_all_asset_id_from_config_rows(self):
        asset_to_deploy_sql = f"""
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
        return self.cursor_fetch(asset_to_deploy_sql)

    def query_keys_id_DISTINCT_from_config_rows(self):
        keypairs_to_deploy_sql = f"""
            SELECT DISTINCT keys_id from config_live_trading
            WHERE status_active = '0'
        """
        return self.cursor_fetch(keypairs_to_deploy_sql)

    def get_asset_by_id(self, asset_id):
        get_asset_by_id_sql = f"""
            SELECT
                assets.id,
                assets.data_provider, 
                assets.ticker, 
                assets.live_data_url,
                assets.live_data_req_body
            FROM assets
            WHERE assets.id = '{asset_id}'
        """
        return self.cursor_fetch(get_asset_by_id_sql)

    def get_key_pair_by_id(self, keys_id):
        get_key_pair_sql = f"""
            SELECT
                exchange_keys.data_provider,
                exchange_keys.api_endpoint,
                exchange_keys.pub_key,
                exchange_keys.priv_key
            FROM exchange_keys
            WHERE exchange_keys.id = '{keys_id}'
        """
        return self.cursor_fetch(get_key_pair_sql)

    def delete_message_id_from_stoped_config_rows(self, config_row_id):
        update_row_sql = f"""
            UPDATE config_live_trading
            SET message_id = 'NULL'
            WHERE id = '{config_row_id}' 
        """
        self.connector.cursor.execute(update_row_sql)
        self.connector.connection.commit()