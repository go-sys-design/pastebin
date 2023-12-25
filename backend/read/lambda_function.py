import logging
import boto3

logger = logging.getLogger("pastebin-read")

def lambda_handler(event, context):
    logger.info("Lambda invoked!")

    try:
        # setup dynamodb
        resource = boto3.resource('dynamodb')
        table = resource.Table('pastebin')

        pasteId = event['PasteId']
        response = table.get_item(Key={
            'PasteId': pasteId
        })

        return {
            'status': 200,
            'message': 'paste found!',
            'data': response['Item']
        }
    
    except Exception as e:
        return {
            'status': 502,
            'message': 'some database error occrred',
            'data': {
                'error': e
            }
        }