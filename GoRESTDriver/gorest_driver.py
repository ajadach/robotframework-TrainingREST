# -*- coding: utf-8 -*-
import requests
import json

from requests.auth import HTTPBasicAuth
from robot.api.deco import keyword


class GoRESTDriver:

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_DOC_FORMAT = 'ROBOT'

    def __init__(self):
        self.url = "https://gorest.co.in/public/v2/users"
        self.url_token = "https://gorest.co.in/public/v2/users?access-token="
        self.headers_user_pwd = {'Accept': 'application/json'}
        self.headers_token = ''
        self.token = ''

    @keyword("Generate Token")
    def generate_token(self, token):
        """ Generate Token. """
        self.token = token
        self.url_token = self.url_token + token
        self.headers_token = {'Authorization': f'Bearer {token}'}

    @keyword("Get: Token In Headers")
    def get_token_in_headers(self):
        """ Get Via Token In Headers

        *Arguments:*
        | =Name= | =Description= | =Example value= |
        | token | If None, use token which is provided by function set_token | token_string_value |

        *Return*
        | payload | dict object from response |
        """
        response = requests.request("GET", url=self.url, headers=self.headers_token, data={})
        return self._logger_response(response)

    @keyword("Get: Token In URL")
    def get_token_in_url(self):
        """ Get Via Token In Headers

        *Arguments:*
        | =Name= | =Description= | =Example value= |
        | token | If None, use token which is provided by function set_token | token_string_value |

        *Return*
        | payload | dict object from response |
        """
        response = requests.request("GET", url=self.url_token, headers=self.headers_token, data={})
        return self._logger_response(response)

    @keyword("Get Via User And Password")
    def get_via_user_and_password(self, user, password):
        """ Get Via User And Password

        *Arguments:*
        | =Name= | =Description= | =Example value= |
        | user | user name | admin |
        | password | password for given user | password |


        *Return*
        | payload | dict object from response |
        """
        response = requests.request("GET", url=self.url, headers=self.headers_user_pwd, auth=HTTPBasicAuth(username=user, password=password))
        return self._logger_response(response)

    def _logger_response(self, response):
        print('=== RESPONSE ===')
        print("Headers:", json.dumps(dict(response.headers), indent=4))
        print("Body:", json.dumps(response.json(), indent=2))
        print("Status Code:", response.status_code, '\n')
        if response.status_code not in [200, 201, 202, 204]:
            raise ValueError("Wrong Status Code")
        return response.json()
