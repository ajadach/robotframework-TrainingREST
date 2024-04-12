from GoRESTDriver.drivers.Common import Common
import requests
import json

from requests.auth import HTTPBasicAuth
from robot.api.deco import keyword


class TokenHeader(Common):

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

    @keyword("Create User: Token In Headers")
    def create_user_token_in_headers(self, name, gender, email, status):
        """ Create User via Token In Headers.

         *Arguments:*
         | =Name= | =Description= | =Example value= |
         | name | name for user | admin |
         | gender | gender male of female | male |
         | email | email for user, need to be unique | example@wp.pl |
         | status | status for new account | active |

         *Return*
         | payload | dict object from response |
         """
        data = {
            'name': name,
            'gender': gender,
            'email': email,
            'status': status,
        }
        response = requests.request("POST", url=self.url, headers=self.headers_token, data=data)
        return self._logger_response(response)

    @keyword("Update User: Token In Headers")
    def update_user_token_in_headers(self, id, name, gender, email, status):
        """ Update User via User And Password.

         *Arguments:*
         | =Name= | =Description= | =Example value= |
         | id | ID for user from database | 6849725 |
         | name | name for user | admin |
         | gender | gender male of female | male |
         | email | email for user, need to be unique | example@wp.pl |
         | status | status for new account | active |

         *Return*
         | payload | dict object from response |
         """
        data = {
            'name': name,
            'gender': gender,
            'email': email,
            'status': status,
        }
        response = requests.request("PATCH", url=self.url_token.replace('users', f'users/{id}'), headers=self.headers_token, data=data)
        return self._logger_response(response)

    @keyword("Delete User: Token In Headers")
    def delete_user_token_in_headers(self, id):
        """ Delete User via User And Password.

         *Arguments:*
         | =Name= | =Description= | =Example value= |
         | id | ID for user from database | 6849725 |

         *Return*
         | payload | dict object from response |
         """
        response = requests.request("DELETE", url=self.url_token.replace('users', f'users/{id}'), headers=self.headers_token, data={})
        return self._logger_response(response)
