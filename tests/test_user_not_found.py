import httpx
import allure

BASE_URL = 'https://reqres.in/api/users'
EMAIL_ENDS = '@reqres.in'


@allure.suite('Проверка запросов с данными пользователей')
@allure.title('Метод, проверяющий ответ на запрос отсутствующего пользователя')
def test_user_nf():
    with allure.step('Выполняем GET запрос'):
        response = httpx.get(BASE_URL + '/23')

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 404