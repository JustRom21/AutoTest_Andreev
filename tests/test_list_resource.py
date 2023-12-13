import httpx
from jsonschema import validate
from core.contracts import RESOURCE_DATA_SCHEMA
import allure

BASE_URL = 'https://reqres.in/api/'


@allure.suite('Проверка запросов с данными ресурсов')
@allure.title('Метод, проверяющий список ресурсов')
def test_list_resource():
    with allure.step('Выполняем GET запрос'):
        response = httpx.get(BASE_URL + 'unknown')

    with allure.step('Проверяем код ответа'):
        assert response.status_code == 200

    resources_data = response.json()['data']
    for item in resources_data:
        with allure.step('Сверяем ответ с контрактом'):
            validate(item, RESOURCE_DATA_SCHEMA)

