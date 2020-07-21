import boto3
import json
import datetime
import pymysql as mariadb

db_name = 'mytestdb'
user_name = 'masteruser'
user_password = 'mymasterpassw0rd1!'
rds_endpoint = 'my-rds-db.czdhqhtfmyqa.us-east-1.rds.amazonaws.com'
db_connection = mariadb.connect(host=rds_endpoint, user=user_name,
password=user_password, database=db_name)

cursor = db_connection.cursor()

try:
    sql = "SELECT * FROM `Users`"
    cursor.execute(sql)
    query_result = cursor.fetchall()
    print('Querying the Users Table...')
    print(query_result)
except mariadb.Error as e:
    print('Error: {}'.format(e))
    print('Sorry, something has gone wrong!')

finally:
    db_connection.close()