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
from threading import Thread
import time



class Servers(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.server = []
        self.iterator = self
        self.index_server = 0
    def update_server(self):
        self.server = []
        temp_servers = Server.list_all(session=SessionLocal())
        if temp_servers:
            for server in temp_servers:
                self.server.append(server)
    def __iter__(self):
        self.index_server = 0
    def __next__(self):
        if self.index_server >= len(self.server):
            self.index_server = 0
        response = self.server[self.index_server]
        self.index_server += 1
        return response
    def get_server(self):
        return next(self.iterator)
    def run(self):
        while True:
            self.update_server()
            time.sleep(10)



class serverManager(object):
    def __init__(self):
        server = Servers()
        server.start()
        self.server = server
    def create_token(self, client_id='cli-web-encoder'):
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
    def check_server(self, uri):
        token = self.create_token()
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


    def upload_server(self, uri):
        picked_server = self.server.get_server()
        payload = {
            'origin': uri
        }
        token = self.create_token()
        if token:
            try:
                headers = {
                    'token': token
                }
                response = requests.post(f'{picked_server.uri}:55001/api/file/create', json=payload, headers=headers, timeout=10)
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


    def status_file(self, name, server_uri):
        token = self.create_token()
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


instance_server_manager = serverManager()


def get_instance_server_manager():
    return instance_server_manager



