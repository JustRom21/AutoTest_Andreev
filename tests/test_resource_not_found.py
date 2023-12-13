import httpx
import allure

BASE_URL = 'https://reqres.in/api/'


@allure.suite('Проверка запросов с данными ресурсов')
@allure.title('Метод, проверяющий ответ на запрос отсутствующего ресурса')
def test_resource_nf():
    with allure.step('Выполняем GET запрос'):
        response = httpx.get(BASE_URL + 'unknown/23')

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 404