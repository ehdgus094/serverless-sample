import json
from lib.python import liblib


def lambda_handler(event, context):
    liblib.run()
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
