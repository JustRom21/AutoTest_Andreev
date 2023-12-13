import httpx
from jsonschema import validate
from core.contracts import RESOURCE_DATA_SCHEMA
import allure

BASE_URL = 'https://reqres.in/api/'


@allure.suite('Проверка запросов с данными ресурсов')
@allure.title('Метод, проверяющий отдельный ресурс')
def test_resource():
    with allure.step('Выполняем GET запрос'):
        response = httpx.get(BASE_URL + 'unknown/2')

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200

    resource_data = response.json()['data']
    with allure.step('Сверяем ответ с контрактом'):
        validate(resource_data, RESOURCE_DATA_SCHEMA)