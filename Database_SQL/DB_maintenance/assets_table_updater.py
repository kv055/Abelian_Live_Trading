import find_parent

from dotenv import load_dotenv
from aws_sql_connect import AWS_SQL, DummyData

from DB_maintenance.Alpaca_assets import all_links_Alpaca
from DB_maintenance.Binance_assets import all_links_Binance
from DB_maintenance.Kraken_assets import all_links_Kraken

# establish connection to the Dummy Data DB
db_connection = DummyData(load_dotenv)

def update_all_pairs_Kraken(connector, values):
    # fetch dataSet from DB
    all_assets_from_DB = f"""SELECT ticker, exchange_name, historical_data_url, live_data_url
        from {connector.DBNAME}.assets WHERE exchange_name = 'Kraken' """
    connector.cursor.execute(all_assets_from_DB)
    table_contents = connector.cursor.fetchall()
    # Check if there are missmatches between the API and the DATABASE
    if table_contents != values:
        pass
    #     # Delete everything in DB, reset id_column and update everything from API
    #     connector.cursor.execute(f"""delete from assets WHERE exchange_name = 'Kraken' """)
    #     connector.connection.commit()

    #     update = f"""update INTO assets (ticker, exchange_name, historical_data_url, live_data_url)
    #         VALUES (%s,%s,%s,%s)"""
    #     connector.cursor.executemany(update,values)
    #     connector.connection.commit()

def update_all_pairs_Binance(connector, values):
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
        # # Delete everything in DB, reset id_column and update everything from API
        # connector.cursor.execute(f"""delete from assets WHERE exchange_name = 'Binance' """)
        # connector.connection.commit()

        # update = f"""update INTO assets (ticker, exchange_name, historical_data_url, live_data_url)
        #     VALUES (%s,%s,%s,%s)"""
        # connector.cursor.executemany(update,values)
        # connector.connection.commit()

def update_all_pairs_Alpaca(connector, values):
    update = f"""insert INTO alpaca_assets (ticker, exchange_name, historical_data_url, live_data_url)
        VALUES (%s,%s,%s,%s)"""
    connector.cursor.executemany(update,values)
    connector.connection.commit()
    

Kraken_URIs = all_links_Kraken()
Binance_URIs = all_links_Binance()
Alpaca_Assets = all_links_Alpaca()


# update_all_pairs_Binance(db_connection, Binance_URIs)
# update_all_pairs_Kraken(db_connection, Kraken_URIs)

update_all_pairs_Binance(db_connection, Binance_URIs)
update_all_pairs_Kraken(db_connection, Kraken_URIs)


lol = 0