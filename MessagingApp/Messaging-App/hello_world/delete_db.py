import boto3
import json

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    for record in event['Records']:
        body = record["body"]
        body1 = json.loads(body)
        
    TABLENAME = dynamodb.Table('mbtis_table')
    response=TABLENAME.delete_item(Key = body1)

    return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Deleted from database"
            })
        }