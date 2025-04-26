import json

def lambda_handler(event, context):
    print("S3 Event Triggered:", json.dumps(event))
    return {"statusCode": 200, "body": "S3 trigger received"}

