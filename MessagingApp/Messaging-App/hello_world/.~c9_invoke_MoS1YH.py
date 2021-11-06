import boto3
import json
import os
sqs = boto3.resource('sqs')


def lambda_handler(event, context):
    
    
    name = event['Name']
    Mbti = event['MBTI']
    
    params: {
        'Name': name,
        'MBTI': Mbti
    }
    print(params)
    queue = sqs.get_queue_by_name(QueueName='test1234')

    response = queue.send_message(MessageBody = json.dumps(params))
    
    print(response)
    return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "MBTI sent to sqs"
            })
        }