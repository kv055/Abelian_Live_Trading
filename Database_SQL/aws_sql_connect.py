import os
import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv

# load_dotenv()

# ENDPOINT = os.getenv('AWSAURORA_ENDPOINT')
# PORT = os.getenv('AWSAURORA_PORT')
# REGION = os.getenv('AWSAURORA_REGION')
# DBNAME = os.getenv('AWSAURORA_DBNAME')
# USER = os.getenv('AWSAURORA_USER')
# ADMINPW = os.getenv('AWSAURORA_ADMINPW')

class AWS_SQL:
    def __init__(self, environement):
        environement()
        ENDPOINT = os.getenv('AWSAURORA_ENDPOINT')
        PORT = os.getenv('AWSAURORA_PORT')
        REGION = os.getenv('AWSAURORA_REGION')
        self.DBNAME = os.getenv('AWSAURORA_DBNAME')
        USER = os.getenv('AWSAURORA_USER')
        ADMINPW = os.getenv('AWSAURORA_ADMINPW')
        
        self.connection = mysql.connector.connect(
            user=USER,
            password=ADMINPW,
            host=ENDPOINT,
            database=self.DBNAME
        )
        # connection.commit()

        self.cursor = self.connection.cursor()
        # cursor.execute()

    def close(self):
        self.connection.close()
    
    
    #def return all tables oder sowas ähnliches
    #def return all columns oder sowas ähnliches

test = AWS_SQL(load_dotenv)



lol = 0


# cnx = mysql.connector.connect(
#     user=USER,
#     password=ADMINPW,
#     host=ENDPOINT,
#     database=DBNAME
# )

# cursor = cnx.cursor()

# # All Tables
# _users = f"SELECT * from {DBNAME}.users"
# _assets = f"SELECT * from {DBNAME}.assets"
# _config_live_trading = f"SELECT * from {DBNAME}.config_live_trading"
# _exchange_keys = f"SELECT * from {DBNAME}.exchange_keys"
# _strategies = f"SELECT * from {DBNAME}.strategies"

# _benutzer = f"SELECT * from {DBNAME}.benutzer"

# _check_all_tables = "SHOW tables;"
# _check_all_columns = f"SHOW COLUMNS FROM {DBNAME}.users"

# cnx.commit()

# cursor.execute(_benutzer)

# rows = cursor.fetchall()
# for r in rows:
#     print(r)

# cnx.close()
