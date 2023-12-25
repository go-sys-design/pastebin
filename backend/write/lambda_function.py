import os
import json
from datetime import datetime
import logging
import boto3
from uuid import uuid4

logger = logging.getLogger("pastebin-write")\

def lambda_handler(event, context):
    logger.info("Lambda invoked!")

    try:
        # setup dynamodb
        resource = boto3.resource('dynamodb')
        table = resource.Table('pastebin')

        # get parameters
        pasteId = str(uuid4())
        userId = event['UserId']
        rawContent = event['content']
        createdTimestamp = int(datetime.now().timestamp()*1000)

        pasteItem = {
            'PasteId': pasteId,
            'TimestampCreated': createdTimestamp,
            'UserId': userId,
            'RawContent': rawContent,
            'ContentURL': ''
        }
        table.put_item(
            Item=pasteItem
        )

    except Exception as e:
        return {
            'status': 502,
            'message': 'some database error occurred',
            'data': {
                'error': e
            }
        }

    return {
        'status': 200,
        'message': 'your paste was successfull',
        'data': pasteItem
    }