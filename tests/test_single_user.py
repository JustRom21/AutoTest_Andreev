import httpx
from jsonschema import validate
from core.contracts import USER_DATA_SCHEMA
import allure

BASE_URL = 'https://reqres.in/api/users'
EMAIL_ENDS = '@reqres.in'


@allure.suite('Проверка запросов с данными пользователей')
@allure.title('Метод проверяющий отдельного пользователя')
def test_user():
    with allure.step('Выполняем GET запрос'):
        response = httpx.get(BASE_URL + '/2')

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200

    user_data = response.json()['data']
    with allure.step('Сверяем ответ с контрактом'):
        validate(user_data, USER_DATA_SCHEMA)

    with allure.step(f'Проверяем, что email оканчивается на {EMAIL_ENDS}'):
        assert user_data['email'].endswith(EMAIL_ENDS)