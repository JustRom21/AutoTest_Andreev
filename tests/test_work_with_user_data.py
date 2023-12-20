import json
import pytest
import httpx
from core.contracts import USER_CREATE_DATA_SCHEMA
from jsonschema import validate
import allure
import datetime

BASE_URL = 'https://reqres.in/api/users/'

@allure.suite('Проверка работы с данными пользователей')
@allure.title('Метод удаления данных пользователя')
def test_delete_user():
    with allure.step('Удаление пользователя'):
        response = httpx.delete(BASE_URL + '2')

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 204

json_file = open('./user_credentials.json')
users_credentials = json.load(json_file)

@pytest.mark.parametrize("user_credentials", users_credentials)
@allure.title('Метод создания данных пользователя')
def test_create_user(user_credentials):
    headers = {'Content-Type': 'Application/json'}
    with allure.step('Создание пользователя'):
        response = httpx.post(BASE_URL, json=user_credentials, headers=headers)

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 201

    resources_data = response.json()
    with allure.step('Сверяем ответ с контрактом'):
        validate(resources_data, USER_CREATE_DATA_SCHEMA)

    response_data = response.json()['createdAt'].replace('T',' ')
    current_data = str(datetime.datetime.utcnow())
    with allure.step('Проверка времени создания'):
        assert response_data[0:16] == current_data[0:16]
