import unittest
from unittest.mock import MagicMock, patch
from lambda_function import lambda_handler
import json

class TestLambdaFunction(unittest.TestCase):

    @patch('boto3.resource')
    def test_post_method(self, mock_resource):
        mock_dynamodb = MagicMock()
        mock_resource.return_value = mock_dynamodb
        event = {
            'httpMethod': 'POST',
            'body': '{"user_name": "test", "email": "test@gmail.com"}'
        }
        # mock_dynamodb.Table.return_value.get_item.return_value = {}
        response = lambda_handler(event, None)

        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(response['body'], '"User registered successfully!"')

    @patch('boto3.resource')
    def test_get_method(self, mock_resource):
        mock_dynamodb = MagicMock()
        mock_resource.return_value = mock_dynamodb
        # mock_table = mock_dynamodb.Table.return_value
        event = {
            'httpMethod': 'GET',
            'body': '{"user_name": "test123"}'
        }
        mock_dynamodb.Table.return_value.query.return_value = {}

        
        response = lambda_handler(event, None)

        self.assertEqual(response['statusCode'], 200)
        
        parsed_body = json.loads(response['body'])
        
        self.assertEqual(parsed_body, [{"user_name": "test123", "email": "test123@gmail.com"}])

    @patch('boto3.resource')
    def test_delete_method(self, mock_resource):
        mock_dynamodb = MagicMock()
        mock_resource.return_value = mock_dynamodb
        event = {
            'httpMethod': 'DELETE',
            'body': '{"user_name": "test", "email": "test@gmail.com"}'
        }
        mock_dynamodb.Table.return_value.delete_item.return_value = {}

        response = lambda_handler(event, None)

        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(response['body'], '"User deleted successfully!"')

if __name__ == '__main__':
    unittest.main()
