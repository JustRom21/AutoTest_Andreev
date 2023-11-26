import httpx
from jsonschema import validate

def test_list_users():
    response = httpx.get('https://reqres.in/api/users?page=2')
    #json_response = response.json()
    #print(json_response['data'])
    assert response.status_code == 200