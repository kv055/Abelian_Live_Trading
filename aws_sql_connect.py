from mysql.connector import errorcode
import mysql.connector
import sys
# import boto3
import os
import pymysql


ENDPOINT = 'abeliantestcase.chrug5fzoy6c.ap-southeast-2.rds.amazonaws.com'
PORT = '3306'
REGION = 'ap-southeast-2b'
DBNAME = 'abeliantestcase'
USER = 'HackerBoi'
ADMINPW = 'StealYoBrowsingHistory'
os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'


cnx = mysql.connector.connect(
    user=USER,
    password=ADMINPW,
    host=ENDPOINT,
    database=DBNAME
)
cursor = cnx.cursor()
_sql = f"SELECT * from {DBNAME}.users"
all_dbs = cursor.execute(_sql)
rows = cursor.fetchall()
for r in rows:
    print(r)
# new_db = cursor.execute("CREATE DATABASE mydatabase")

cnx.close()


# try:
#     cnx = mysql.connector.connect(
#         user=USER,
#         password=ADMINPW,
#         host=ENDPOINT,
#         database=DBNAME
#     )
#
# except mysql.connector.Error as err:
#     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#         print("Something is wrong with your user name or password")
#     elif err.errno == errorcode.ER_BAD_DB_ERROR:
#         print("Database does not exist")
#     else:
#         print(err)
# else:
#     cnx.close()
#

# first_connection = pymysql.connect(
#     'abeliantestcase.chrug5fzoy6c.ap-southeast-2.rds.amazonaws.com'
#     'abeliantestcase',
#     'StealYoBrowsingHistory'
# )

# cursor = first_connection.cursor()


# gets the credentials from .aws/credentials
# session = boto3.Session(profile_name='default')
# client = session.client('rds')


# client = boto3.client('rds',REGION)

# token = client.generate_db_auth_token(
#     DBHostname=ENDPOINT,
#     Port=PORT,
#     DBUsername=USER,
#     Region=REGION
# )

# try:
#     conn =  mysql.connector.connect(host=ENDPOINT, user=USER, passwd=token, port=PORT, database=DBNAME, ssl_ca='SSLCERTIFICATE')
#     cur = conn.cursor()
#     cur.execute("""SELECT now()""")
#     query_results = cur.fetchall()
#     print(query_results)
# except Exception as e:
#     print("Database connection failed due to {}".format(e))
