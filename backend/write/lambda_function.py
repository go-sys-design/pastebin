import os
import json
import logging
import boto3

is_prod = os.environ['PROD'] == '1'

logger = logging.getLogger("pastebin-write")
logger.setLevel(logging.INFO if is_prod else logging.DEBUG)

def lambda_handler(event, context):
    logger.info("Lambda invoked finally!", os.environ['PROD'])

    return {
        'status': 200,
        'message': 'working'
    }