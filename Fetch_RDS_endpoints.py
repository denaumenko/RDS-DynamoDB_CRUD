import boto3
import json
import datetime

def date_time_converter(o):
    if isinstance(o, datetime.datetime):
        return  o.__str__()

rds_identifier = 'my-rds-db'

rds_client = boto3.client('rds',
    aws_access_key_id="*****",
    aws_secret_access_key="***")

print("Fetching the RDS endpoint...")
response = rds_client.describe_db_instances(
    DBInstanceIdentifier=rds_identifier
)

rds_endpoint = json.dumps(response['DBInstances'][0]['Endpoint']['Address'])
rds_endpoint = rds_endpoint.replace('"','')
print('RDS Endpoint: ' + rds_endpoint)