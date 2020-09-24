import boto3

session = boto3.Session(profile_name='personal')
ec2_client = session.client('ec2', region_name='us-east-1')

response = ec2_client.describe_instances()
print(response)
