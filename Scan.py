import boto3
import json
import datetime
import uuid
# Create a DynamoDB Resource
dynamodb_resource = boto3.resource('dynamodb',
                    aws_access_key_id = "****",
                    aws_secret_access_key = "****"
)


table = dynamodb_resource.Table('Users')
# Let's do a scan!
response = table.scan()
print('The total Count is: ' + json.dumps(response['Count']))
print(json.dumps(response['Items'], indent=2, sort_keys=True))