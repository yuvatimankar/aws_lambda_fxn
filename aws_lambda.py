import boto3

def lambda_handler(event, context):
    # TODO implement
    client = boto3.client('ssm')
    response = client.get_parameter(Name='external-api-url')
    
    return{
        'statusCode':200,
        'body': response['Parameter']['Value']
    }