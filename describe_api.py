import boto3

client = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')

table_name = 'users'
table = dynamodb.Table(table_name)
Primary_Column_Name = 'user_id'
Primary_Key = '346fdfggw4' 
Columns = ['first_name', 'age', 'last_name']

# Describe_API

response = client.describe_table(TableName = table_name)
print(response)

# Query_Parameter