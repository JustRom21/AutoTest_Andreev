import json
import pytest
import httpx
from jsonschema import validate
import allure

BASE_URL = 'https://reqres.in/api/users?delay=3'

@allure.title('Проверка позднего ответа')
def test_delayed_response():
    response = httpx.get(BASE_URL, timeout=4)

    with allure.step('Проверяем код ответа'):
        assert response.status_code ==200
