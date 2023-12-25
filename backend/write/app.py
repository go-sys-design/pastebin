import os
import jsonpickle
import logging
import boto3

is_prod = os.environ['PROD'] == '1'

logger = logging.getLogger("pastebin-write")
logger.setLevel(logging.INFO if is_prod else logging.DEBUG)

def lambda_handler(event, context):
    logger.info('## ENVIRONMENT VARIABLES\r' + jsonpickle.encode(dict(**os.environ)))
    logger.info('## EVENT\r' + jsonpickle.encode(event))
    logger.info('## CONTEXT\r' + jsonpickle.encode(context))

    return {
        'status': 200,
        'message': 'working'
    }