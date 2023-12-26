import httpx
from core.contracts import LOGIN_CREATE_DATA_SCHEMA
from jsonschema import validate
import allure

LOGIN_URL = 'https://reqres.in/api/login'

@allure.suite('Проверка логина')
@allure.title('Проверка успешного логина')
def test_success_login():
    users_login_pass = {"email": "eve.holt@reqres.in","password": "cityslicka"}
    headers = {'Content-Type': 'Application/json'}
    response = httpx.post(LOGIN_URL, json=users_login_pass, headers=headers)

    resources_data = response.json()
    with allure.step('Сверяем ответ с контрактом'):
        validate(resources_data, LOGIN_CREATE_DATA_SCHEMA)

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200

@allure.title('Проверка логина без пароля')
def test_login_missing_pass():
    users_login_pass = {"email": "eve.holt@reqres.in"}
    headers = {'Content-Type': 'Application/json'}
    response = httpx.post(LOGIN_URL, json=users_login_pass, headers=headers)

    with allure.step('Проверка текста ошибки'):
        assert response.json()['error'] == 'Missing password'

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 400

@allure.title('Проверка неправильного пароля')
def test_login_wrong_login():
    users_login_pass = {"email": "e2ve.holt@reqres.in","password": "cityslicka"}
    headers = {'Content-Type': 'Application/json'}
    response = httpx.post(LOGIN_URL, json=users_login_pass, headers=headers)

    with allure.step('Проверка текста ошибки'):
        assert response.json()['error'] == 'user not found'

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 400

