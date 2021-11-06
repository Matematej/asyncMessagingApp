import boto3
import json

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    
    ITEM = event['Records'][0['body']
    print(ITEM)
    TABLENAME = dynamodb.Table('orders_table')
    TABLENAME.put_item(Item = ITEM)

    return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "MBTI sent to database"
            })
        }

