import json
import pytest
import httpx
import allure

BASE_URL = 'https://reqres.in/api/register'

json_file = open('./register_unsuccess_credentials.json')
register_unsuccess_credentials = json.load(json_file)

@pytest.mark.parametrize("register_unsuccess_credentials", register_unsuccess_credentials)
@allure.suite('Проверка работы регистрации')
@allure.title('Метод создания данных регистрации без пароля')
def test_create_register_unsuccess(register_unsuccess_credentials):
    headers = {'Content-Type': 'Application/json'}
    with allure.step('Создание пользователя'):
        response = httpx.post(BASE_URL, json=register_unsuccess_credentials, headers=headers)


    with allure.step('Проверяем код ответа'):
        assert response.status_code == 400