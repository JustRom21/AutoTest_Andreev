import httpx
from core.contracts import USER_CREATE_DATA_SCHEMA
from jsonschema import validate
import allure

BASE_URL = 'https://reqres.in/api/users/'

@allure.suite('Проверка работы с данными пользователей')
@allure.title('Метод удаления данных пользователя')
def test_delete_user():
    with allure.step('Удаление пользователя'):
        response = httpx.delete(BASE_URL + '2')

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 204

@allure.title('Метод создания данных пользователя')
def test_create_user():
    headers = {'Content-Type': 'Application/json'}
    Name = "Roman"
    Job = "QA"
    body = {"name": Name,"job": Job}
    with allure.step('Создание пользователя'):
        response = httpx.post(BASE_URL, json=body, headers=headers)

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 201

    resources_data = response.json()
    with allure.step('Сверяем ответ с контрактом'):
        validate(resources_data, USER_CREATE_DATA_SCHEMA)

    with allure.step('Проверяем переданное имя'):
        assert response.json()['name'] == Name

    with allure.step('Проверяем переданную должность'):
        assert response.json()['job'] == Job