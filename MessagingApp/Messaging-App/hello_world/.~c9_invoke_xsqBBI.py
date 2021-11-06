import boto3
import json
import os
sqs = boto3.resource('sqs')


def lambda_handler(event, context):
    
    Item = event
    
    queue = sqs.get_queue_by_name(QueueName='test1234')

    response = queue.send_message(MessageBody = event)

    print(queue)
    
    return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "MBTI sent to sqs"
            })
        }

    