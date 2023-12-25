import pytest
from lambda_function import lambda_handler

def test_success():
    pasteId = 'b76386c0-2771-42eb-b259-c3f392bbe0d1'

    response = lambda_handler(
        event={
            'PasteId': pasteId
        }, 
        context={}
    )

    assert response['status'] == 200
