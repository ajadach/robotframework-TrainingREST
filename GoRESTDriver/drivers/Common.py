# -*- coding: utf-8 -*-
import requests
import json

from requests.auth import HTTPBasicAuth
from robot.api.deco import keyword


class Common:

    def __init__(self):
        self.url = "https://gorest.co.in/public/v2/users"
        self.url_token = "https://gorest.co.in/public/v2/users?access-token="
        self.headers_user_pwd = {'Accept': 'application/json'}
        self.headers_token = ''
        self.token = ''
        self.user = ''
        self.password = ''

    @keyword("Generate Token")
    def generate_token(self, token):
        """ Generate Token. """
        self.token = token
        self.url_token = self.url_token + token
        self.headers_token = {'Authorization': f'Bearer {token}'}

    def login(self, user, password):
        self.user = user
        self.password = password

    def _logger_response(self, response):
        print('=== RESPONSE ===')
        print("Headers:", json.dumps(dict(response.headers), indent=4))

        print("Status Code:", response.status_code, '\n')
        if response.status_code not in [200, 201, 202, 204]:
            raise ValueError("Wrong Status Code")
        try:
            print("Body:", json.dumps(response.json(), indent=2))
            return response.json()
        except Exception:
            pass
