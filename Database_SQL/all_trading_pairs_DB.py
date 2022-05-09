from dotenv import load_dotenv
import requests
from aws_sql_connect import AWS_SQL


# Connection
db_connection = AWS_SQL(load_dotenv)


def all_pairs_Kraken():
    request_all_Kraken_pairs = requests.get('https://api.kraken.com/0/public/AssetPairs')
    Kraken_pairs_raw = request_all_Kraken_pairs.json()
    
    Kraken_pairs = []
    # names = []

    for pair in Kraken_pairs_raw['result']:
        Kraken_pairs.append(pair)
    return Kraken_pairs

def all_pairs_Binance():
    request_all_Binance_pairs = requests.get('https://api.binance.com/api/v3/exchangeInfo')
    Binance_pairs_raw = request_all_Binance_pairs.json()

    Binance_pairs = []
    # names = []

    for pair in Binance_pairs_raw['symbols']:
        Binance_pairs.append(pair['symbol'])
    Binance_pairs.sort()
    return Binance_pairs

def all_links_Kraken():
    pairs = all_pairs_Kraken()
    live_data_URIs = []
    ohlc_data_URIs = []
    for pair in pairs:
        ohlc_data_URI = 'https://api.kraken.com/0/public/OHLC?pair='+pair+'&interval='
        ohlc_data_URIs.append(ohlc_data_URI)
        live_data_URI = 'https://api.kraken.com/0/public/Ticker?pair='+pair
        live_data_URIs.append(live_data_URI)

    # return tuples
    db_format_content = []
    if len(pairs) == len(ohlc_data_URIs) == len(live_data_URIs):
        for i in range(0, len(pairs)):
            db_format_content.append(
                (pairs[i],ohlc_data_URIs[i],live_data_URIs[i])
            )

    return db_format_content

def all_links_Binance():
    pairs = all_pairs_Binance()
    live_data_URIs = []
    ohlc_data_URIs = []
    for pair in pairs:
        ohlc_data_URI = 'https://api.binance.com/api/v3/klines?symbol='+pair+'&interval='
        ohlc_data_URIs.append(ohlc_data_URI)
        live_data_URI = 'https://api.binance.com/api/v3/ticker/price?symbol='+pair
        live_data_URIs.append(live_data_URI)
    
    # return tuples
    db_format_content = []
    if len(pairs) == len(ohlc_data_URIs) == len(live_data_URIs):
        for i in range(0, len(pairs)):
            db_format_content.append(
                (pairs[i],ohlc_data_URIs[i],live_data_URIs[i])
            )
            
    return db_format_content

def insert_all_pairs(connector, values, sql):
    # Fetch whole list from db and compare before inserting new one
    connector.cursor.execute(sql,values)
    connector.connection.commit()

    

Kraken_pairs = all_pairs_Kraken()
Binance_pairs = all_pairs_Binance()

Kraken_URIs = all_links_Kraken()
Binance_URIs = all_links_Binance()

sql_insert_kraken = f"""INSERT INTO kraken_assets (ticker, historicel_data_url, live_data_url) VALUES (%s,%s,%s)"""
sql_insert_binance = f"""INSERT INTO binance_assets (ticker, historicel_data_url, live_data_url) VALUES (%s,%s,%s)"""

insert_all_pairs(db_connection, Kraken_URIs, sql_insert_kraken)
insert_all_pairs(db_connection, Binance_URIs, sql_insert_binance)

lol = 0

# look  for matching records for potential assets only DB
# Kraken_set = set(Kraken_pairs)
# Binance_set = set(Binance_pairs)
# intersections = Binance_set.intersection(Kraken_set)