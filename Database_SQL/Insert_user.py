from dotenv import load_dotenv
from aws_sql_connect import AWS_SQL


# Connection
db_connection = AWS_SQL(load_dotenv)

# Data
user = {
    'first_name': 'Kilian',
    'last_name': 'Voss',
    'e_mail': 'kilian96@live.de'
}

def insert_user(connector):
    # Data
    user = {
        'first_name': 'Kilian',
        'last_name': 'Voss',
        'e_mail': 'kilian96@live.de'
    }
    ins = f"""INSERT INTO users (first_name, last_name, e_mail) VALUES (%s,%s,%s)"""
    val = (user['first_name'],user['last_name'],user['e_mail'])
    connector.cursor.execute(ins, val)
    connector.connection.commit()
    # implement error handling or any feedback from db


insert_user(db_connection, user)