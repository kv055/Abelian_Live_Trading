import mysql.connector
import sys
import boto3
import os

ENDPOINT = 'abeliantestcase.chrug5fzoy6c.ap-southeast-2.rds.amazonaws.com'
PORT = '3306'
REGION ='ap-southeast-2b'
DBNAME = 'abeliantestcase'
USER = 'HackerBoi'
os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'

#gets the credentials from .aws/credentials
session = boto3.Session(profile_name='default')
client = session.client('rds')

token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT, DBUsername=USER, Region=REGION)

try:
    conn =  mysql.connector.connect(host=ENDPOINT, user=USER, passwd=token, port=PORT, database=DBNAME, ssl_ca='SSLCERTIFICATE')
    cur = conn.cursor()
    cur.execute("""SELECT now()""")
    query_results = cur.fetchall()
    print(query_results)
except Exception as e:
    print("Database connection failed due to {}".format(e))          