import unittest
import datetime
import requests
import responses

from Verify.HttpStatusCode import HttpStatus
from Verify.logger import Log
from Verify.verify import Verify


class TestMockedAPI(unittest.TestCase):
    url = "http://localhost:5000"

    @responses.activate
    def test_create_user(self):
        current_utc_time = datetime.datetime.utcnow()
        formatted_time = current_utc_time.strftime('%Y-%m-%d %H:%M:%S')
        # Mock response data
        mock_response = {
            "id": 123,
            "name": "John Doe",
            "job": "Engineer",
            "createdAt": formatted_time
        }

        mock_url = f'{self.url}/create_user/Selim/Engineer'

        responses.add(responses.POST, mock_url, status=201, json={
            "createdAt": "2024-07-08T14:40:11.998Z",
            "id": "2103",
            "job": "Software QA Engineer",
            "name": "Selim Erdinç"
        })

        payload = {
            'job': 'Software QA Engineer',
            'name': 'Selim Erdinç'
        }
        response = requests.post(mock_url, json=payload)

        Verify.assert_status_code(response, HttpStatus.CREATED)

        Verify.assert_json_data(response, {
            "createdAt": "2024-07-08T14:40:11.998Z",
            "id": "2103",
            "job": "Software QA Engineer",
            "name": "Selim Erdinç"
        })

        Log.test_pass(self._testMethodName)

    @responses.activate
    def test_register_user(self):
        # Mock response data
        mock_response = {
            "id": 1903,
            "token": "tokentoken2103"
        }

        # Mock API endpoint
        mock_url = 'http://localhost:5000/register_user'

        # Add a mock response
        responses.add(responses.POST, mock_url, json=mock_response, status=200)

        payload = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        # Perform a POST request to the mock server
        response = requests.post(mock_url, json=payload)

        Verify.assert_status_code(response, HttpStatus.OK)

        Verify.assert_json_data(response, {
            "id": 1903,
            "token": "tokentoken2103"
        })

        Log.test_pass(self._testMethodName)


if __name__ == '__main__':
    unittest.main()
