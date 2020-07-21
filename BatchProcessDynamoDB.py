import boto3
import json
import datetime
import uuid


dynamodb_resource = boto3.resource('dynamodb',aws_access_key_id = "****",
                    aws_secret_access_key = "*****")

table = dynamodb_resource.Table('Users')
# Generate some random data
with table.batch_writer() as user_data:
    for i in range(100):
        user_data.put_item(
        Item={
            'user_id': str(uuid.uuid4()),
            'user_email': 'someone' + str(i) + '@somewhere.com',
            'user_fname': 'User' + str(i),
            'user_lname': 'UserLast' + str(i)
        }
)
print('Writing record # ' + str(i+1) + ' to DynamoDB Users Table')
print('Done!')