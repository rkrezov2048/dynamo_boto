import boto3

# create a client object
client = boto3.client('dynamodb')
table_name = 'users'
# create a resource objcet

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)
Primary_Column_Name = 'user_id'
Primary_Key = '346fdfggw4' 
Columns = ['first_name', 'age', 'last_name']
Delete_Key = '2345delete_me'

# Get Item API
response = table.get_item(
    Key = {
        Primary_Column_Name:Primary_Key
    }
)

print(response['Item'])


# Primary_Key = 'gfgjry45645'
# Put Item API
# response = table.put_item(
#     Item = {
#         Primary_Column_Name:Primary_Key,
#         Columns[0]: 'Michael',
#         Columns[1]: '39',
#         Columns[2]: 'Blevins'
#     }
# )

# print(response)

#  Delete Item API
response = table.delete_item(
    Key = {
        Primary_Column_Name: Delete_Key
    }
)

print(response)