import boto3


client = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')

table_name = 'users'
Primary_Column_Name = 'user_id'
table = dynamodb.Table(table_name)
id = 'gfgjry45645'


# How to do a query
from boto3.dynamodb.conditions import Key
response = table.query(
    KeyConditionExpression = Key(Primary_Column_Name).eq(id)
)

items = response['Items']
print(items)