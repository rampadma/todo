import os

import boto3


def put_item(item, dynamodb=None):

    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url=os.getenv('dynamodb_url'))

    todo_table = dynamodb.Table('todo')
    response = todo_table.put_item(Item=item)
    return response


def delete_item(item):
    pass


def query(item):
    pass


def get_by_id(id):
    pass
