import find_parent
from dotenv import load_dotenv
from Database_SQL.aws_sql_connect import AWS_SQL


# Connection
db_connection = AWS_SQL(load_dotenv)


def querry(connector):
    # All Tables
    _users = f"SELECT * from {connector.DBNAME}.users"
    _assets = f"SELECT * from {connector.DBNAME}.assets"
    _config_live_trading = f"SELECT * from {connector.DBNAME}.config_live_trading"
    _exchange_keys = f"SELECT * from {connector.DBNAME}.exchange_keys"
    _strategies = f"SELECT * from {connector.DBNAME}.strategies"

    _benutzer = f"SELECT * from {connector.DBNAME}.benutzer"

    _check_all_tables = "SHOW tables;"
    _check_all_columns = f"SHOW COLUMNS FROM {connector.DBNAME}.users"

    connector.cursor.execute(_check_all_tables)
    rows = connector.cursor.fetchall()
    for r in rows:
        print(r)


querry(db_connection)