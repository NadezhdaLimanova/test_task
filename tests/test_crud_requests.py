# tests/test_crud_requests

import pytest
from api_classes.api import RequestsAPI
from api_classes.models import RegisterUser

class TestCRUDRequests:
    """Класс для тестирования методов создания, удаления и обновления"""


    def test_create_user(self, base_url):
        body = RegisterUser.random()
        response = RequestsAPI(url=base_url).create_user(body=body)
        response_body = response.json()

        assert response.status_code == 201
        assert response.headers['Content-Type'].startswith("application/json")
        assert "id" in response_body
        assert response_body["name"] == body["name"]
        assert response_body["job"] == body["job"]


    @pytest.mark.parametrize("page", [("1"), ("2"), ("3")])
    def test_update_user(self, base_url, page):
        body = RegisterUser.random()
        response = RequestsAPI(url=base_url).update_user(page, body=body)
        response_body = response.json()

        assert response.status_code == 200
        assert response.headers['Content-Type'].startswith("application/json")
        assert response_body["name"] == body["name"]
        assert response_body["job"] == body["job"]


    @pytest.mark.parametrize("page", [("1"), ("2"), ("3")])
    def test_partial_update_user(self, base_url, page):
        body = RegisterUser.random()
        response = RequestsAPI(url=base_url).update_user(page, body=body)
        response_body = response.json()

        assert response.status_code == 200
        assert response.headers['Content-Type'].startswith("application/json")
        assert response_body["name"] == body["name"]
        assert response_body["job"] == body["job"]


    @pytest.mark.parametrize("page", [("1"), ("2"), ("3")])
    def test_delete_user(self, base_url, page):
        response = RequestsAPI(url=base_url).delete_user(page)

        assert response.status_code == 204
