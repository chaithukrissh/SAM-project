import boto3

dynamodb = boto3.resource('dynamodb')

table_name = 'UserRegistrationTable'

table = dynamodb.create_table(
    TableName=table_name ,
    KeySchema=[
        {
        'AttributeName': 'user_name',
        'KeyType': 'HASH'  
    },
    {
        'AttributeName': 'email',
        'KeyType': 'RANGE'  
    }
    ] ,
     AttributeDefinitions = [
     {
         'AttributeName': 'user_name',
         'AttributeType': 'S'  
     },
     {
         'AttributeName': 'email',
         'AttributeType': 'S' 
     }, 

    ] ,
    
    BillingMode='PAY_PER_REQUEST'
   
)


table.meta.client.get_waiter('table_exists').wait(TableName=table_name)

print(f'Table {table_name} created successfully!')

