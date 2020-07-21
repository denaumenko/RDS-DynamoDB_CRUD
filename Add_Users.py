import boto3
import uuid
import json
import datetime


dynamodb_resource = boto3.resource('dynamodb',
                                   aws_access_key_id="***",
                                   aws_secret_access_key="****"
                                   )
table = dynamodb_resource.Table('Users')
# Write a record to DynamoDB
response = table.put_item(
Item={
'user_id': '1234-5678',
'user_email': 'someone@somewhere.com',
'user_fname': 'Sam',
'user_lname': 'Samuels'
}
)

print(json.dumps(response, indent=2, sort_keys=True))