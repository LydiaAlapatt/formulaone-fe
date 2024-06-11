import boto3

def initialize_database():
    session = boto3.Session()
    dynamo_resource = session.resource(
        'dynamodb',
        region_name='eu-west-1'
    )
    return dynamo_resource