import boto3
import json
import datetime

rds_identifier = 'my-rds-db'
sg_name = 'rds-sg-dev-demo'
sg_id_number = ''

rds_client = boto3.client('rds', aws_access_key_id="****",
                          aws_secret_access_key="***"
                          )
# Delete the RDS Instance
response = rds_client.delete_db_instance(
DBInstanceIdentifier=rds_identifier,
SkipFinalSnapshot=True)

print('RDS Instance is being terminated...This may take several minutes.')

waiter = rds_client.get_waiter('db_instance_deleted')
waiter.wait(DBInstanceIdentifier=rds_identifier)

print('The Amazon RDS database has been deleted. Removing Security Groups')

ec2_client = boto3.client('ec2',
                          aws_access_key_id="****",
                          aws_secret_access_key="***"
                          )

response = ec2_client.describe_security_groups(
    GroupNames=[
    sg_name
])
sg_id_number = json.dumps(response['SecurityGroups'][0]['GroupId'])
sg_id_number = sg_id_number.replace('"','')

response = ec2_client.delete_security_group(
    GroupId=sg_id_number
)

print('Cleanup is complete!')