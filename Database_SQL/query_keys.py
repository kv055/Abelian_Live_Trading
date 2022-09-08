def keys(connector,trading_config):
    api_keys = []
    for user_id in trading_config:
        index = user_id
        query =  f"SELECT * from {connector.DBNAME}.exchange_keys WHERE id = {index}"
        connector.cursor.execute(query)
        table = connector.cursor.fetchall()
        return_obj = {
            'user_id': table[0][1],
            'keys_id': user_id,
            'endpoint': table[0][4],
            'api_endpoint': table[5],
            'pub_key': table[0][2],
            'priv_key': table[0][3],
        }
        api_keys.append(return_obj)

    return api_keys
