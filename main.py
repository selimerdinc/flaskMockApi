import datetime

from flask import Flask, jsonify, request
import requests
from flasgger import Swagger
from API.UserApi.GetUser import *
from API.UserApi.PostUser import *

app = Flask(__name__)
swagger = Swagger(app)


@app.route('/')
def home():
    return "Mock API'ye hoş geldiniz!"


@app.route('/users', methods=['GET'])
def get_users():
    """
    Reqres.in API'sinden kullanıcıları getir
    ---
    responses:
      200:
        description: Kullanıcı verileri
        schema:
          type: object
          properties:
            data:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  email:
                    type: string
                  first_name:
                    type: string
                  last_name:
                    type: string
                  avatar:
                    type: string
    """
    data = {
        "page": 1,
        "per_page": 1,
        "total": 1,
        "total_pages": 1,
        "data": [
            {
                "id": 1,
                "email": "selimerdinc1@selimerdinc.com",
                "first_name": "Selim",
                "last_name": "Erdinç",
                "avatar": "my_avatar"
            }],
        "support": {
            "url": "https://github.com/selimerdinc",
            "linkedin": "https://www.linkedin.com/in/selimerdinc/",
            "superpeer": "https://superpeer.com/selimerdinc",
        }
    }
    return jsonify(data)


@app.route('/single_user/<int:user_id>', methods=['GET'])
def get_single_user(user_id):
    """
    Reqres.in API'sinden tek bir kullanıcıyı getir
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: Kullanıcı ID'si
    responses:
      200:
        description: Tek bir kullanıcı verisi
        schema:
          type: object
          properties:
            data:
              type: object
              properties:
                id:
                  type: integer
                email:
                  type: string
                first_name:
                  type: string
                last_name:
                  type: string
                avatar:
                  type: string
    """
    data = {
        "data": {
            "id": user_id,
            "email": "selimerdinc@selimerdinc.com",
            "first_name": "Selim",
            "last_name": "Erdinç",
            "avatar": "my_avatar"
        },
        "support": {
            "url": "https://github.com/selimerdinc",
            "linkedin": "https://www.linkedin.com/in/selimerdinc/",
            "superpeer": "https://superpeer.com/selimerdinc",
        }
    }
    return jsonify(data)


new_user_schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'job': {'type': 'string'}
    },
    'required': ['name', 'job']
}


@app.route('/create_user/<string:name>/<string:job>', methods=['POST'])
def create_user(name, job):
    """
    Yeni bir kullanıcı oluşturur.
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            job:
              type: string
    responses:
      201:
        description: Yeni kullanıcı oluşturuldu
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            job:
              type: string
            createdAt:
              type: string
    """
    result = {'name': 'selimerdinc@selimerdinc.com', 'job': 'Software QA Engineer', 'id': '1903',
              'createdAt': '2024-07-08T15:08:04.788Z'}
    return jsonify(result), 201


new_register_schema = {
    'type': 'object',
    'properties': {
        'email': {'type': 'string'},
        'password': {'type': 'string'}
    },
    'required': ['email', 'password']
}


@app.route('/register_user', methods=['POST'])
def register_user():
    """
    Yeni bir kullanıcı oluşturur.
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            email:
              type: string
            password:
              type: string
    responses:
      200:
        description: Yeni kullanıcı oluşturuldu
        schema:
          type: object
          properties:
            id:
              type: integer
            token:
              type: string
    """
    result = {'id': 1903, 'token': 'selimmock'}
    return jsonify(result), 200

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Kullanıcıyı günceller.
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: Kullanıcı ID'si
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            job:
              type: string
    responses:
      200:
        description: Kullanıcı güncellendi
        schema:
          type: object
          properties:
            name:
              type: string
            job:
              type: string
            updatedAt:
              type: string
    """
    data = request.get_json()
    name = data.get('name')
    job = data.get('job')
    updated_at = datetime.datetime.utcnow().isoformat() + 'Z'

    response_data = {
        "name": name,
        "job": job,
        "updatedAt": updated_at
    }

    return jsonify(response_data), 200




@app.route('/api/users/<int:user_id>', methods=['PATCH'])
def patch_user(user_id):
    """
    Kullanıcıyı günceller.
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: Kullanıcı ID'si
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
    responses:
      200:
        description: Kullanıcı güncellendi
        schema:
          type: object
          properties:
            name:
              type: string
            updatedAt:
              type: string
    """
    data = request.get_json()
    name = data.get('name')

    if not name:
        return jsonify({"error": "Name field is required"}), 400

    updated_at = datetime.datetime.utcnow().isoformat() + 'Z'

    user_data = get_single_user_from_reqres(user_id)

    if 'error' in user_data:
        return jsonify({"error": "User not found"}), 404

    response = requests.patch(f"https://reqres.in/api/users/{user_id}", json={"name": name})
    if response.status_code == 200:
        response_data = {
            "name": name,
            "updatedAt": updated_at
        }
        return jsonify(response_data), 200
    else:
        return jsonify({"error": "Failed to update user"}), response.status_code


@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Kullanıcıyı siler.
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: Kullanıcı ID'si
    responses:
      204:
        description: Kullanıcı başarıyla silindi
      404:
        description: Kullanıcı bulunamadı
    """

    user_data = get_single_user_from_reqres(user_id)

    if 'error' in user_data:
        return jsonify({"error": "User not found"}), 404

    response = requests.delete(f"https://reqres.in/api/users/{user_id}")

    if response.status_code == 204:
        return {"detail":"user-deleted"}
    else:
        return jsonify({"error": "Failed to delete user"}), response.status_code
    
@app.errorhandler(404)
def not_found_error(e):
    """
    404 hatalarını loglar ve tekrar API'den veri getirir.
    """
    print(f"404 Error: Request path - {request.full_path}")

    response = requests.get(f"https://reqres.in/api{request.full_path}")

    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({"error": "Data not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
