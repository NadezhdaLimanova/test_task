# api_classes/api.py

import requests
import logging
logger = logging.getLogger("api")

class Register:
    def __init__(self, url):
        self.url = url

    POST_REGISTER_USER = '/register'

    def register_user(self, body: dict):
        """
        https://reqres.in/api/register
        """
        response = requests.post(f"{self.url}{self.POST_REGISTER_USER}", json=body)
        logger.info(response.text)
        return response


class GetUser:
    def __init__(self, url):
        self.url = url

    GET_USER = '/users'
    GET_RESOURCE = '/unknown'

    def get_single_user(self, params=None):
        """
        https://reqres.in/api/users/2
        """
        response = requests.get(f"{self.url}{self.GET_USER}{params}")
        logger.info(response.text)
        return response

    def get_list_users(self, params=None):
        """
        https://reqres.in/api/users?page=2
        """
        response = requests.get(f"{self.url}{self.GET_USER}", params=params)
        logger.info(response.text)
        return response


    def get_list_resource(self):
        """
        https://reqres.in/api/unknown
        """
        response = requests.get(f"{self.url}{self.GET_RESOURCE}")
        logger.info(response.text)
        return response

    def get_single_resource(self, params=None):
        """
        https://reqres.in/api/unknown/2
        """
        response = requests.get(f"{self.url}{self.GET_RESOURCE}{params}")
        logger.info(response.text)
        return response

