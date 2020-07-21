import boto3
import json
import datetime
import pymysql as mariadb


rds_identifier = 'my-rds-db'

db_name = 'mytestdb'
user_name = 'masteruser'
user_password = 'mymasterpassw0rd1!'
rds_endpoint = 'my-rds-db.****.us-east-1.rds.amazonaws.com'

db_connection = mariadb.connect(host=rds_endpoint, user=user_name,
    password=user_password, database=db_name)

cursor = db_connection.cursor()

try:
    cursor.execute("CREATE TABLE Users (user_id INT NOT NULL AUTO_INCREMENT,"
                   "user_fname VARCHAR(100) NOT NULL, "
                   "user_lname VARCHAR(150) NOT NULL,"
                   "user_email VARCHAR(175) NOT NULL, "
                   "PRIMARY KEY(`user_id`))")
    print('Table Created!')
except mariadb.Error as e:
    print('Error: {}'.format(e))
finally:
    db_connection.close()

db_connection = mariadb.connect(host=rds_endpoint, user=user_name,
password=user_password, database=db_name)
cursor = db_connection.cursor()

try:
    sql = "INSERT INTO `Users` (`user_fname`, `user_lname`, `user_email`) VALUES (% s, % s, % s)"
    cursor.execute(sql, ('CJ', 'Smith', 'casey.smith@somewhere.com'))
    cursor.execute(sql, ('Casey', 'Smith', 'sam.smith@somewhere.com'))
    cursor.execute(sql, ('No', 'One', 'no.one@somewhere.com'))
    db_connection.commit()
    print('Inserted Data to Database!')
except mariadb.Error as e:
    print('Error: {}'.format(e))
    print('Sorry, something has gone wrong!')
finally:
    db_connection.close()
