import boto3
import json
import datetime

dynamodb_resource = boto3.resource('dynamodb',
    aws_access_key_id="AKIA3LV3C62V3RWAMNV5",
    aws_secret_access_key="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")
table = dynamodb_resource.create_table(
    TableName='Users',
    KeySchema=[
        {
            'AttributeName': 'user_id',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'user_email',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'user_id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'user_email',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

print("The DynamoDB Table is being created, this may take a few minutes...")
table.meta.client.get_waiter('table_exists').wait(TableName='Users')
print("Table is ready!")