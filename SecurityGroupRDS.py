import boto3
import json
import datetime

sg_name = "rds-sg-dev-demo"
sg_description =  "RDS Security Group for AWS Dev Study Guide"
my_ip_cidr = '0.0.0.0/0'

ec2_client = boto3.client('ec2',
                          aws_access_key_id='*******',
                          aws_secret_access_key='****'
                          )

response = ec2_client.create_security_group(
    Description=sg_description,
    GroupName=sg_name
)

print(json.dumps(response,indent=2, sort_keys=True))

response = ec2_client.authorize_security_group_ingress(
    CidrIp=my_ip_cidr,
    FromPort=3306,
    GroupName=sg_name,
    ToPort=3306,
    IpProtocol='tcp'
)

print("Security Group should be created! Verify this in the AWS Console.")
