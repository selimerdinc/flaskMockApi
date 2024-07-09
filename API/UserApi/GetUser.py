import requests


def get_user_from_reqres():
    response = requests.get("https://reqres.in/api/users?page=2")
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Veri çekilemedi"}

def get_single_user_from_reqres(user_id):
    response = requests.get(f"https://reqres.in/api/users/{user_id}")
    if response.status_code == 200:
        user_data = response.json().get('data', {})
        return {
            'name': user_data.get('first_name', '') + ' ' + user_data.get('last_name', ''),
        }
    else:
        return {"error": "Veri çekilemedi"}