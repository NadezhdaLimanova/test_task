# tests/test_login_registration

import pytest
from api_classes.api import LoginRegister


class TestsLoginRegistration:
    """Класс для тестирования методов при регистрации и введении логина"""

    @pytest.mark.parametrize("email, password", [("eve.holt@reqres.in", "cityslicka"),
                                                 ("janet.weaver@reqres.in", "password123")])
    def test_registration(self, base_url, email, password):
        body = {
            "email": email,
            "password": password
        }
        response = LoginRegister(url=base_url).register_user(body=body)

        assert response.status_code == 200


    @pytest.mark.parametrize("email", [("sydney@fife"), ("abcdefg@hijk")])
    def test_registration_unsuccesful(self, base_url, email):
        body = {
            "email": email
        }
        response = LoginRegister(url=base_url).register_user(body=body)
        response_body = response.json()

        assert response.status_code == 400
        assert response_body['error'] == "Missing password"


    @pytest.mark.parametrize("email, password", [("eve.holt@reqres.in", "cityslicka"),
                                                 ("janet.weaver@reqres.in", "password123")])
    def test_login(self, base_url, email, password):
        body = {
            "email": email,
            "password": password
        }
        response = LoginRegister(url=base_url).login_user(body=body)

        assert response.status_code == 200

    @pytest.mark.parametrize("email", [("peter@klaven"), ("abcdefg@hijk")])
    def test_login_unsuccesful(self, base_url, email):
        body = {
            "email": email
        }
        response = LoginRegister(url=base_url).login_user(body=body)
        response_body = response.json()

        assert response.status_code == 400
        assert response_body['error'] == "Missing password"
