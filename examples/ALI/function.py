import json


def handler(event, context):
    return {
        'event': event,
        'context': context,
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
