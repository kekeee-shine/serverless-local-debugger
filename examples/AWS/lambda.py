import json


def lambda_handler(event, context):
    # TODO implement
    return {
        'event': event,
        'context': context,
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
