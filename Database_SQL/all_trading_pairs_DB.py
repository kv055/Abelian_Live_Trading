from dotenv import load_dotenv
import requests
from aws_sql_connect import AWS_SQL, DummyData


# establish connection to the Dummy Data DB
db_connection = DummyData(load_dotenv)

# Fetch all tradable asset pairs
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

# Create URL's to fetch price Data
def all_links_Kraken():
    pairs = all_pairs_Kraken()
    exchange_name = 'Kraken'
    live_data_URIs = []
    ohlc_data_URIs = []
    for pair in pairs:
        ohlc_data_URI = 'https://api.kraken.com/0/public/OHLC?pair='+pair+'&interval='
        ohlc_data_URIs.append(ohlc_data_URI)
        live_data_URI = 'https://api.kraken.com/0/public/Ticker?pair='+pair
        live_data_URIs.append(live_data_URI)

    # return tuples so that it can be inserted
    db_format_content = []
    if len(pairs) == len(ohlc_data_URIs) == len(live_data_URIs):
        for i in range(0, len(pairs)):
            db_format_content.append(
                (pairs[i],exchange_name,ohlc_data_URIs[i],live_data_URIs[i])
            )

    return db_format_content

def all_links_Binance():
    pairs = all_pairs_Binance()
    exchange_name = 'Binance'
    live_data_URIs = []
    ohlc_data_URIs = []
    for pair in pairs:
        ohlc_data_URI = 'https://api.binance.com/api/v3/klines?symbol='+pair+'&interval='
        ohlc_data_URIs.append(ohlc_data_URI)
        live_data_URI = 'https://api.binance.com/api/v3/ticker/price?symbol='+pair
        live_data_URIs.append(live_data_URI)
    
    # return tuples so that it can be inserted
    db_format_content = []
    if len(pairs) == len(ohlc_data_URIs) == len(live_data_URIs):
        for i in range(0, len(pairs)):
            db_format_content.append(
                (pairs[i],exchange_name,ohlc_data_URIs[i],live_data_URIs[i])
            )
            
    return db_format_content

def insert_all_pairs_Kraken(connector, values):
    # fetch dataSet from DB
    all_assets_from_DB = f"""SELECT ticker, exchange_name, historical_data_url, live_data_url
        from {connector.DBNAME}.assets WHERE exchange_name = 'Kraken' """
    connector.cursor.execute(all_assets_from_DB)
    table_contents = connector.cursor.fetchall()
    # Check if there are missmatches between the API and the DATABASE
    if table_contents != values:
        pass
    #     # Delete everything in DB, reset id_column and insert everything from API
    #     connector.cursor.execute(f"""delete from assets WHERE exchange_name = 'Kraken' """)
    #     connector.connection.commit()

    #     insert = f"""INSERT INTO assets (ticker, exchange_name, historical_data_url, live_data_url)
    #         VALUES (%s,%s,%s,%s)"""
    #     connector.cursor.executemany(insert,values)
    #     connector.connection.commit()

def insert_all_pairs_Binance(connector, values):
    # fetch dataSet from DB
    all_assets_from_DB = f"""SELECT ticker, exchange_name, historical_data_url, live_data_url
        from {connector.DBNAME}.assets WHERE exchange_name = 'Binance' """
    connector.cursor.execute(all_assets_from_DB)
    table_contents = connector.cursor.fetchall()
    # Check if there are missmatches between the API and the DATABASE
    table_contents_set = []
    for index in range(0, len(table_contents)):
        tuple_to_convert = values[index]
        set_to_push = set(tuple_to_convert)
        table_contents_set.append(set_to_push)
        print(set_to_push)
    for index in range(0, len(table_contents)):
        tuple_to_convert = values[index]
        set_to_push = set(tuple_to_convert)
        table_contents_set.append(set_to_push)
        print(set_to_push)
    if table_contents != values:
        pass
        # # Delete everything in DB, reset id_column and insert everything from API
        # connector.cursor.execute(f"""delete from assets WHERE exchange_name = 'Binance' """)
        # connector.connection.commit()

        # insert = f"""INSERT INTO assets (ticker, exchange_name, historical_data_url, live_data_url)
        #     VALUES (%s,%s,%s,%s)"""
        # connector.cursor.executemany(insert,values)
        # connector.connection.commit()

Kraken_URIs = all_links_Kraken()
Binance_URIs = all_links_Binance()


# insert_all_pairs_Binance(db_connection, Binance_URIs)
# insert_all_pairs_Kraken(db_connection, Kraken_URIs)

insert_all_pairs_Binance(db_connection, Binance_URIs)
insert_all_pairs_Kraken(db_connection, Kraken_URIs)

lol = 0

###############################################################################################
# pseudo_code sketches


# look  for matching records for potential assets only DB
# Kraken_set = set(Kraken_pairs)
# Binance_set = set(Binance_pairs)
# intersections = Binance_set.intersection(Kraken_set)

# def insert_assets_DB(connector, values, exchange_name):
# # fetch dataSet from DB    
# all_assets_from_DB = f"""SELECT ticker, exchange_name, historical_data_url, live_data_url
#         from {connector.DBNAME}.assets WHERE exchange_name = 'Binance' """
#     connector.cursor.execute(all_assets_from_DB)
#     table_contents = connector.cursor.fetchall()
    
#     bool = table_contents != values
#     # Check if there are missmatches between the API and the DATABASE
#     if table_contents != values:
#         # Delete everything in DB, reset id_column and insert everything from API
#         connector.cursor.execute(f"""delete from assets WHERE exchange_name = 'Binance' """)
#         connector.connection.commit()

#         insert = f"""INSERT INTO assets (ticker, exchange_name, historical_data_url, live_data_url)
#             VALUES (%s,%s,%s,%s)"""
#         connector.cursor.executemany(insert,values)
#         connector.connection.commit()