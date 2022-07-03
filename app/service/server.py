import requests
from app.config import(
    SERVER_USERNAME,
    SERVER_PASSWORD,
    SERVER_AUTH
)

from app.models.domain.server import Server
from app.models.domain.file import File
from app.core.database import SessionLocal

import random


def create_token(client_id='cli-web-encoder'):
    try:
        headers = {
            'Content-Type': 'multipart/form-data'
        }
        payload = {
            'username': SERVER_USERNAME,
            'password': SERVER_PASSWORD,
            'client_id': client_id
        }
        response = requests.post(f'{SERVER_AUTH}/auth/token', data=payload, headers={}, timeout=10)
        if response.status_code == 200:
            return response.json()['access_token']
    except Exception as err:
        print(f'exception create token - {err}')
    return False




def check_server(uri):
    token = create_token()
    if token:
        headers = {
            'token': token
        }
        try:
            response = requests.get(f'{uri}:55001/api/file/list', headers=headers, timeout=10)
            if response.status_code == 200:
                return True
        except Exception as err:
            print(f'exception checkk server - {err}')
    return False


def upload_server(uri):
    temp_servers = Server.list_all(session=SessionLocal())
    if temp_servers:
        picked_server = random.choices(temp_servers)
        temp_token = create_token()
        payload = {
            'origin': uri
        }
        try:
            response = requests.post(picked_server.uri, json=payload, timeout=10)
            if response.status_code == 200:
                if response.json().get('status', False) == 200:
                    temp_file = File.add_file(session=SessionLocal(), 
                                                name=response.json()['data']['name'], 
                                                server=picked_server.id
                    )
                    return temp_file
        except Exception as err:
            print(f'upload_server exception - {err}')
    return False


def status_file(name, server_uri):
    token = create_token()
    if token:
        try:
            headers = {
                'token': token
            }
            response = requests.get(f'{server_uri}:55001/api/file/see?name={name}', headers=headers, timeout=10)
            if response.status_code == 200:
                return response.json().get('data', False)
        except Exception as err:
            print(f'service.server.status_file exception - {err}')
    return False