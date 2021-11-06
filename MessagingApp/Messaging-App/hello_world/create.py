import boto3
import json
import os
sqs = boto3.resource('sqs')


def lambda_handler(event, context):
    
    name = event['Name']
    Mbti = event['MBTI']
    
    params= json.dumps({"Name": name, "MBTI": Mbti})
    print(params)
    queue = sqs.get_queue_by_name(QueueName='MBTIQueue')
    print(queue.url)
    
    response = queue.send_message(MessageBody= params)
    
    return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "MBTI sent to sqs"
            })
        }