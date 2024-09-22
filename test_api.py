import requests
import pytest

@pytest.fixture()
def id_obj():
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    response = requests.post('https://reqres.in/api/register', json=payload).json()
    yield response['id']
    requests.delete(f'https://reqres.in/api/register/{response['id']}')

def test_post_object():
    payload = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
    }

    response = requests.post('https://reqres.in/api/register', json=payload).json()
    assert response['token'] == 'QpwL5tke4Pnpja7X4'


def test_get_object(id_obj):
    response = requests.get(f'https://reqres.in/api/register/{id_obj}').json()
    assert response['data']['id'] == id_obj



def test_put_object(id_obj):
    payload = {
        "email": "redhotchilli@gmail.com",
        "password": "rock"
        }
    response = requests.put(f'https://reqres.in/api/register/{id_obj}', json=payload).json()
    assert response['email'] == payload['email']
    assert response['password'] == payload['password']


def test_delete_object(id_obj):
    response = requests.delete(f'https://reqres.in/api/register/{id_obj}')
    assert response.status_code == 204
    response = requests.get(f'https://reqres.in/api/register/{id_obj}')
    assert response.status_code == 200