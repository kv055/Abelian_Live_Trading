user = {
    'first_name': 'Kilian',
    'last_name': 'Voss',
    'e-mail': 'kilian96@live.de'
}

def insert_user(connector, user_dict):
    # %s, %s, %s
    ins = f"""INSERT INTO benutzer (name) VALUES ('Joes')"""
    # val = ("Juhn","sfskj","dfifdi")
    connector.cursor.execute(ins)

keys = {
    'user_id': 69,
    'exchange_id': 69,
    'exchange_id': 69,
    'pub_key': 420,
    'priv_key': 420
}

def insert_exchange_keys(connector, keys_dict):
    pass

config = {
    'user_id': 69,
    'strategy_id': 69,
    'asset_id': 69
}

def insert_config(connector, config_dict):
    ins = f"""INSERT INTO benutzer (name) VALUES ('Joes')"""
    # val = ("Juhn","sfskj","dfifdi")
    connector.cursor.execute(ins)
    pass

asset = {
    'aset_name': 'BitchCoin'
}

def insert_assets(connector, asset_dict):
    pass



