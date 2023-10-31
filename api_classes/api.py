import requests
import logging
logger = logging.getLogger("api")


class LoginRegister:
    """Класс для основных методов работы с API при регистрации и введении логина"""
    def __init__(self, url):
        self.url = url

    POST_REGISTER_USER = 'api/register'
    POST_LOGIN_USER = 'api/login'

    def register_user(self, body: dict):
        """
        https://reqres.in/api/register
        """
        response = requests.post(f"{self.url}{self.POST_REGISTER_USER}", json=body)
        logger.info(response.text)
        return response

    def login_user(self, body: dict):
        """
        https://reqres.in/api/login
        """
        response = requests.post(f"{self.url}{self.POST_LOGIN_USER}", json=body)
        logger.info(response.text)
        return response


class RequestsAPI:
    """Класс для основных методов работы с API при запросе информации, создании, удалении или обновлении"""
    def __init__(self, url):
        self.url = url

    CRUD_USER = 'api/users/'
    RESOURSE_LIST = 'api/'

    def get_single_user(self, page):
        """
        https://reqres.in/api/users/2
        """
        response = requests.get(f"{self.url}{self.CRUD_USER}{page}")
        logger.info(response.text)
        return response


    def get_list_users(self, page):
        """
        https://reqres.in/api/users?page=2
        """
        response = requests.get(f"{self.url}{self.CRUD_USER}?page={page}")
        logger.info(response.text)
        return response


    def create_user(self, body: dict):
        """
        https://reqres.in/api/users
        """
        response = requests.post(f"{self.url}{self.CRUD_USER}", json=body)
        logger.info(response.text)
        return response

#
    def update_user(self, page, body: dict):
        """
        https://reqres.in/api/users/2
        """
        response = requests.put(f"{self.url}{self.CRUD_USER}{page}", json=body)
        logger.info(response.text)
        return response


    def partial_update_user(self, page, body: dict):
        """
        https://reqres.in/api/users/2
        """

        response = requests.patch(f"{self.url}{self.CRUD_USER}{page}", json=body)
        logger.info(response.text)
        return response


    def delete_user(self, page):
        """
        https://reqres.in/api/users/2
        """
        response = requests.delete(f"{self.url}{self.CRUD_USER}{page}")
        logger.info(response.text)
        return response


    def get_list_resource(self, page):
        """
        https://reqres.in/api/unknown
        """
        response = requests.get(f"{self.url}{self.RESOURSE_LIST}{page}")
        logger.info(response.text)
        return response

    def get_single_resource(self, page, number):
        """
        https://reqres.in/api/unknown/2
        """
        response = requests.get(f"{self.url}{self.RESOURSE_LIST}{page}/{number}")
        logger.info(response.text)
        return response

    def delayed_response(self, delay):
        """
        https://reqres.in/api/users?page=2
        """
        response = requests.get(f"{self.url}{self.CRUD_USER}?delay={delay}")
        logger.info(response.text)
        return response

