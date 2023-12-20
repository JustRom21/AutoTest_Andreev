import json
import pytest
import httpx
from core.contracts import REGISTER_CREATE_DATA_SCHEMA
from jsonschema import validate
import allure

BASE_URL = 'https://reqres.in/api/register'

json_file = open('./register_credentials.json')
register_credentials = json.load(json_file)

@pytest.mark.parametrize("register_credentials", register_credentials)
@allure.suite('Проверка работы регистрации')
@allure.title('Метод создания данных регистрации')
def test_create_register(register_credentials):
    headers = {'Content-Type': 'Application/json'}
    with allure.step('Создание пользователя'):
        response = httpx.post(BASE_URL, json=register_credentials, headers=headers)
        print(response.json())

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200

    resources_data = response.json()
    with allure.step('Сверяем ответ с контрактом'):
        validate(resources_data, REGISTER_CREATE_DATA_SCHEMA)

