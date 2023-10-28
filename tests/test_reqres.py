import pytest
from api_classes.api import Register, GetUser
import time

@pytest.fixture
def base_url() -> str:
    return 'https://reqres.in/api'


class TestsRegistration:

    def test_registration(self, base_url, params=None):
        if params is None:
            body = {
                "email": "eve.holt@reqres.in",
                "password": "pistol"
            }
        response = Register(url=base_url).register_user(body=body)
        assert response.status_code == 200


    @pytest.mark.xfail
    def test_registration_fail(self, base_url, params=None):
        if params is None:
            body = {
                "email": "sydney@fife"
            }
        response = Register(url=base_url).register_user(body=body)
        assert response.status_code == 400
        assert response.body['error'] == "Missing password"


class TestsGetUsers:

    def test_get_list_users(self, base_url, params=None):
        if params is None:
            params = {'page': 2}

        response = GetUser(url=base_url).get_list_users(params)
        response_body = response.json()

        assert response.status_code == 200
        assert response.headers['Content-Type'].startswith("application/json")
        assert len(response.json()) > 0
        assert response_body["data"][0]["last_name"] == "Lawson"


    def test_get_single_user(self, base_url, params=None):
        if params is None:
            params = '/2'

        response = GetUser(url=base_url).get_single_user(params)
        response_body = response.json()

        assert response.status_code == 200
        assert response.headers['Content-Type'].startswith("application/json")
        assert len(response.json()) > 0
        assert response_body["data"]["last_name"] == "Weaver"


    def test_delayed_responce(self, base_url, params=None):
        if params is None:
            params = {'delay': 3}

        start_time = time.time()
        response = GetUser(url=base_url).get_list_users(params)
        end_time = time.time()

        assert end_time - start_time >= 3


    @pytest.mark.xfail
    def test_single_user_fail(self, base_url, params=None):
        if params is None:
            params = '/23'

        response = GetUser(url=base_url).get_single_user(params)

        assert response.status_code == 400
        assert len(response.json()) == 0


    def test_get_list_resourse(self, base_url):
        response = GetUser(url=base_url).get_list_resource()
        response_body = response.json()

        assert response.status_code == 200
        assert response.headers['Content-Type'].startswith("application/json")
        assert len(response.json()) > 0
        assert response_body["data"][0]["name"] == "cerulean"


    def test_get_single_resource(self, base_url, params=None):
        if params is None:
            params = '/2'

        response = GetUser(url=base_url).get_single_resource(params)
        response_body = response.json()

        assert response.status_code == 200
        assert response.headers['Content-Type'].startswith("application/json")
        assert len(response.json()) > 0
        assert response_body["data"]["name"] == "fuchsia rose"


    @pytest.mark.xfail
    def test_get_single_resource_fail(self, base_url, params=None):
        if params is None:
            params = '/23'

        response = GetUser(url=base_url).get_single_resource(params)

        assert response.status_code == 400
        assert len(response.json()) == 0







# def test_get_list_users(base_url, params=None):
#
#     if params is None:
#         params = {'page': 2}
#
#     response = requests.get(base_url + "/api/users", params=params)
#     response_body = response.json()
#
#     assert response.status_code == 200
#     assert response.headers['Content-Type'].startswith("application/json")
#     assert len(response.json()) > 0
#     assert response_body["data"][0]["last_name"] == "Lawson"
#
#
# def test_get_single_user(base_url):
#
#     response = requests.get(base_url + "/api/users/2")
#     response_body = response.json()
#
#     assert response.status_code == 200
#     assert response.headers['Content-Type'].startswith("application/json")
#     assert len(response.json()) > 0
#     assert response_body["data"]["last_name"] == "Weaver"
#
# def test_list_resourse(base_url):
#
#     response = requests.get(base_url + "/api/unknown")
#     response_body = response.json()
#
#     assert response.status_code == 200
#     assert response.headers['Content-Type'].startswith("application/json")
#     assert len(response.json()) > 0
#     assert response_body["data"][0]["name"] == "cerulean"
#
# def test_single_resourse(base_url):
#
#     response = requests.get(base_url + "/api/unknown/2")
#     response_body = response.json()
#
#     assert response.status_code == 200
#     assert response.headers['Content-Type'].startswith("application/json")
#     assert len(response.json()) > 0
#     assert response_body["data"]["name"] == "fuchsia rose"
#
# def test_create_user(base_url, params=None):
#
#     if params is None:
#         params = {
#             "name": "morpheus",
#                   "job": "leader"
#         }
#
#     response = requests.get(base_url + "/api/users")
#     response_body = response.json()
#
#     assert response.status_code == 201
#     assert response.headers['Content-Type'].startswith("application/json")
#         assert response_body["data"]["name"] == "fuchsia rose"
