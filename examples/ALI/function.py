import json


def handler(event, context):
    return {
        'event': json.loads(event.decode()),
        'context': context,
        'statusCode': 200,
        'body': json.dumps('Hello from Function!')
    }
