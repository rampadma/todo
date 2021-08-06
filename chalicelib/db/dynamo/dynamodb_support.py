import json
import os
import traceback

import boto3
from botocore.exceptions import ClientError
from chalice import ChaliceViewError, BadRequestError


def put_item(table_name: str, item, dynamodb=None):
    try:
        print("Inserting into table {}, value {}", table_name, json.dumps(item))
        get_dynamodb_table(table_name, dynamodb).put_item(Item=item)
    except ClientError as ce:
        traceback.print_exc()
        print(ce.response['Error']['Message'])
    except Exception as e:
        traceback.print_exc()
        raise e


def update_item(table_name: str, key, expression, attribute_names, attribute_values, dynamodb=None):
    try:
        return get_dynamodb_table(table_name, dynamodb).update_item(Key=key, UpdateExpression=expression,
                                                                    ExpressionAttributeNames=attribute_names,
                                                                    ExpressionAttributeValues=attribute_values,
                                                                    ReturnValues="UPDATED_NEW")
    except ClientError as ce:
        traceback.print_exc(ce)
        print(ce.response['Error']['Message'])
        raise ChaliceViewError(ce.response['Error']['Message'])
    except Exception as e:
        traceback.print_exc()
        raise e


def delete_item(table_name: str, key: dict, dynamodb=None):
    try:
        return get_dynamodb_table(table_name, dynamodb).delete_item(Key={'id': key})
    except ClientError as ce:
        traceback.print_exc(ce)
        print(ce.response['Error']['Message'])
        raise ChaliceViewError(ce.response['Error']['Message'])
    except Exception as e:
        traceback.print_exc()
        raise e


def query(table_name: str, condition_expression, dynamodb=None):
    try:
        return get_dynamodb_table(table_name, dynamodb).query(**condition_expression)['Items']
    except ClientError as ce:
        traceback.print_exc()
        print(ce.response['Error']['Message'])
        raise ChaliceViewError(ce.response['Error']['Message'])
    except Exception as e:
        traceback.print_exc()
        raise e


def get_by_id(table_name: str, key: str, dynamodb=None):
    try:
        result = get_dynamodb_table(table_name, dynamodb).get_item(Key={
            'id': key
        })
        if 'Item' in result:
            return result['Item']
        raise BadRequestError('Id {} not found'.format(key))
    except ClientError as ce:
        traceback.print_exc()
        print(ce.response['Error']['Message'])
        raise ChaliceViewError(ce.response['Error']['Message'])
    except Exception as e:
        traceback.print_exc()
        raise e


def get_all_items(table_name: str, dynamodb=None):
    pass


def get_dynamodb_table(table_name: str, dynamodb):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-west-1', endpoint_url=os.getenv('dynamodb_url'))

    return dynamodb.Table(table_name)
