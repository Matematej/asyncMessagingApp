import boto3
import json
import os
sqs = boto3.resource('sqs')


def lambda_handler(event, context):
    decoded_event=json.loads(event['body'])
    name = decoded_event['Name']

    params= json.dumps({"Name": name})
    print(params)
    queue = sqs.get_queue_by_name(QueueName='DeleteMBTIQueue')
    print(queue.url)
    
    response = queue.send_message(MessageBody= params)
    
    return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Delete request sent to sqs"
            })
        }