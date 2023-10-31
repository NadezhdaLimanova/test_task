# tests/test_get_requests

import pytest
from api_classes.api import RequestsAPI
import time


class TestsGetRequests:
    """Класс для тестирования основных запросов"""

    @pytest.mark.parametrize("page", [("1"), ("2"), ("3")])
    def test_get_list_users(self, base_url, page):
        response = RequestsAPI(url=base_url).get_list_users(page)
        response_body = response.json()

        assert response.status_code == 200
        assert response.headers['Content-Type'].startswith("application/json")
        assert len(response.json()) > 0
        assert str(response_body["page"]) == page


    @pytest.mark.parametrize("page", [("1"), ("2"), ("3")])
    def test_get_single_user(self, base_url, page):
        response = RequestsAPI(url=base_url).get_single_user(page)
        response_body = response.json()

        assert response.status_code == 200
        assert response.headers['Content-Type'].startswith("application/json")
        assert len(response.json()) > 0
        assert str(response_body['data']["id"]) == page


    @pytest.mark.parametrize("delay", [("3"), ("4"), ("5")])
    def test_delayed_response(self, base_url, delay):
        start_time = time.time()
        RequestsAPI(url=base_url).delayed_response(delay)
        end_time = time.time()

        assert end_time - start_time >= 3



    @pytest.mark.parametrize("page", [("23"), ("24"), ("445")])
    def test_get_single_user_not_found(self, base_url, page):
        response = RequestsAPI(url=base_url).get_single_user(page)

        assert response.status_code == 404
        assert len(response.json()) == 0


    @pytest.mark.parametrize("page", [("fsghsrt3"), ("2tjrj4"), ("unknown")])
    def test_get_list_resource(self, base_url, page):
        response = RequestsAPI(url=base_url).get_list_resource(page)
        response_body = response.json()

        assert response.status_code == 200
        assert response.headers['Content-Type'].startswith("application/json")
        assert len(response.json()) > 0
        assert response_body["page"] == 1


    @pytest.mark.parametrize("page, number", [("fsghsrt3", "2"), ("2tjrj4", "3"), ("unknown", "5")])
    def test_get_single_resource(self, base_url, page, number):
        response = RequestsAPI(url=base_url).get_single_resource(page, number)
        response_body = response.json()

        assert response.status_code == 200
        assert response.headers['Content-Type'].startswith("application/json")
        assert len(response.json()) > 0
        assert str(response_body['data']["id"]) == number


    @pytest.mark.parametrize("page, number", [("fsghsrt3", "27"), ("2tjrj4", "34"), ("unknown", "52")])
    def test_get_single_resource_not_found(self, base_url, page, number):
        response = RequestsAPI(url=base_url).get_single_resource(page, number)

        assert response.status_code == 404
        assert len(response.json()) == 0