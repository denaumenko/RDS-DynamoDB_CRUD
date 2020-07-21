import boto3
from boto3.dynamodb.conditions import Key
import json
import datetime
# Create a DynamoDB Resource
dynamodb_resource = boto3.resource('dynamodb',
    aws_access_key_id="****",
    aws_secret_access_key="*****")
table = dynamodb_resource.Table('Users')
# Query a some data
response = table.query(
    KeyConditionExpression=Key('user_id').eq('1234-5678'),
)
# Print the data out!
print(json.dumps(response['Items'], indent=2, sort_keys=True))