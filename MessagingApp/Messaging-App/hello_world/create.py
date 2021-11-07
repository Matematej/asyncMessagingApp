import boto3
import json
import os
sqs = boto3.resource('sqs')


def lambda_handler(event, context):
    decoded_event=json.loads(event['body'])
    name = decoded_event["Name"]
    Mbti = decoded_event["MBTI"]
    params={"Name": name, "MBTI": Mbti}
    print(params)
    queue = sqs.get_queue_by_name(QueueName='MBTIQueue')
    print(queue.url)
    
    response = queue.send_message(MessageBody=json.dumps(params))
    
    return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "MBTI sent to sqs"
            })
        }