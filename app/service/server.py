import requests
from app.config import(
    SERVER_USERNAME,
    SERVER_PASSWORD,
    SERVER_AUTH
)


def create_token(client_id='cli-web-encoder'):
    try:
        print('try crate token')
        headers = {
            'Content-Type': 'multipart/form-data'
        }
        payload = {
            'username': SERVER_USERNAME,
            'password': SERVER_PASSWORD,
            'client_id': client_id
        }
        response = requests.post(f'{SERVER_AUTH}/auth/token', data=payload, headers={}, timeout=10)
        print(response)
        print(response.text)
        if response.status_code == 200:
            return response.json()['access_token']
    except Exception as err:
        print(f'exception create token - {err}')
    return False




def check_server(uri):
    token = create_token()
    if token:
        print(token)
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