import json
import boto3


dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    name = event["queryStringParameters"]['Name']
    
    TABLENAME = dynamodb.Table('mbtis_table')
    response = TABLENAME.get_item(Key={'Name': name})
    return {
            "statusCode": 200,
            "body": json.dumps({
               "Item": response['Item']
           })
        }