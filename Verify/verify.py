class Verify:
    @staticmethod
    def assert_status_code(response, expected_status_code):
        assert response.status_code == expected_status_code, f"Expected status code {expected_status_code}, but got {response.status_code}"

    @staticmethod
    def assert_json_contains(response, expected_keys):
        json_data = response.json()
        for key in expected_keys:
            assert key in json_data, f"Expected key '{key}' not found in JSON response"

    @staticmethod
    def assert_json_data(response, expected_data):
        json_data = response.json()
        for key, value in expected_data.items():
            assert key in json_data, f"Expected key '{key}' not found in JSON response"
            assert json_data[key] == value, f"Expected value '{value}' for key '{key}', but got '{json_data[key]}'"
