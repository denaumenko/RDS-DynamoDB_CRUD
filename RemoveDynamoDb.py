
import boto3
import json
import datetime
import uuid
# Create a DynamoDB Resource
dynamodb_client = boto3.client('dynamodb',
                    aws_access_key_id = "****",
                    aws_secret_access_key = "***")

# Delete the Table
response = dynamodb_client.delete_table(TableName='Users')
print(json.dumps(response, indent=2, sort_keys=True))