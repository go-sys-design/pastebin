import pytest
from lambda_function import lambda_handler

expected_fields = ['PasteId', 'UserId', 'TimestampCreated', 'RawContent', 'ContentURL']

def test_success():
    userId = 'harin'
    content = 'testing with pytest'
    
    response = lambda_handler(
        event={
            'UserId': userId,
            'content': content
        },
        context={}
    )

    added_item = response['data']

    assert response['status'] == 200
    assert sorted(list(added_item)) == sorted(expected_fields)
    assert added_item['UserId'] == userId
    assert added_item['RawContent'] == content

def test_failure():
    response = lambda_handler({}, {})
    assert response['status'] != 200