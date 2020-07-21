import boto3
import json
import datetime

def date_time_converter(o):
    if isinstance(o, datetime.datetime):
        return  o.__str__()

sg_name = "rds-sg-dev-demo"
rds_identifier = 'my-rds-db'
db_name = 'mytestdb'
user_name = 'masteruser'
user_password = 'mymasterpassw0rd1!'
admin_email = 'myemail@myemail.com'
sg_id_number = ''
rds_endpoint = ''

ec2_client = boto3.client('ec2',aws_access_key_id="****",aws_secret_access_key="****")


response = ec2_client.describe_security_groups(
    GroupNames=[
        sg_name
    ])

sg_id_number = json.dumps(response['SecurityGroups'][0]['GroupId'])
sg_id_number = sg_id_number.replace('"','')

rds_client = boto3.client('rds',aws_access_key_id="***",aws_secret_access_key="***")



response = rds_client.create_db_instance(
    DBInstanceIdentifier=rds_identifier,
    DBName=db_name,
    DBInstanceClass='db.t2.micro',
    Engine='mariadb',
    MasterUsername='masteruser',
    MasterUserPassword='mymasterpassw0rd1!',
    VpcSecurityGroupIds=[
        sg_id_number
    ],
    AllocatedStorage=20
)

print('Creating the RDS instance. This may take several minutes...')
waiter = rds_client.get_waiter('db_instance_available')
waiter.wait(DBInstanceIdentifier=rds_identifier)
print('Okay! The Amazon RDS Database is up!')