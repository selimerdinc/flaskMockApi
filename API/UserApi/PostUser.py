import requests


def post_user(name, job):
    payload = {"name": name, "job": job}
    response = requests.post("https://reqres.in/api/users", json=payload)
    if response.status_code == 201:
        return response.json()
    else:
        return {"error": "Veri gönderilemedi"}


def post_user_register(email, password):
    payload = {"email": email, "password": password}
    response = requests.post("https://reqres.in/api/register", json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Veri gönderilemedi"}
