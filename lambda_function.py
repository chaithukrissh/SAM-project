import json
import boto3
from boto3.dynamodb.conditions import Key


dynamodb = boto3.resource('dynamodb')

table_name = 'UserRegistrationTable'
table = dynamodb.Table(table_name)


def lambda_handler(event, context):
    try:
        if event['httpMethod'] == 'POST':
            body = json.loads(event['body'])
            user_name = body['user_name']
            email = body['email']

            table.put_item(
                Item={
                    'user_name': user_name,
                    'email': email
                }
            )

            response = {
                'statusCode': 200,
                'body': json.dumps('User registered successfully!')
            }

        elif event['httpMethod'] == 'GET':
            try:
    
                    data = json.loads(event['body'])
                    user_name = data.get('user_name')

                    
                    if user_name : 
                        
                        response = table.query(
                            KeyConditionExpression=Key('user_name').eq(user_name)  
                        )

                        
                        items = response.get('Items', [])

                        if items:
                            return {
                                'statusCode': 200,
                                'body': json.dumps(items)
                            }
                        else:
                            return {
                                'statusCode': 404,
                                'body': json.dumps({'error': 'Items not found'})
                            }
                    else:
                        return {
                            'statusCode': 400,
                            'body': json.dumps({'error': 'user_name is required in the request body.'})
                        }

            except Exception as e:
                return {
                    'statusCode': 500,
                    'body': json.dumps({'error': f'Error: {str(e)}'})
                }

        elif event['httpMethod'] == 'DELETE':
            body = json.loads(event['body'])
            user_name = body['user_name']
            email = body['email']

            if user_name:
                table.delete_item(
                    Key={
                        'user_name': user_name ,
                        'email':email
                    }
                )

                return {
                    'statusCode': 200,
                    'body': json.dumps('User deleted successfully!')
                }
            else:
                return {
                    'statusCode': 404,
                    'body': json.dumps('User not found!')
                }
            

        else:
            response = {
                'statusCode': 400,
                'body': json.dumps('Invalid HTTP method')
            }

    except Exception as e:
        response = {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }

    return response
