from GoRESTDriver.drivers.Common import Common
import requests
import json

from requests.auth import HTTPBasicAuth
from robot.api.deco import keyword


class UserPwd(Common):

    @keyword("Get Via User And Password")
    def get_via_user_and_password(self):
        """ Get Via User And Password

        *Arguments:*
        | =Name= | =Description= | =Example value= |
        | user | user name | admin |
        | password | password for given user | password |


        *Return*
        | payload | dict object from response |
        """
        response = requests.request("GET", url=self.url, headers=self.headers_user_pwd, auth=HTTPBasicAuth(username=self.user, password=self.password))
        return self._logger_response(response)

    @keyword("Create User: User And Password")
    def create_user_via_user_and_password(self, name, gender, email, status):
        """ Create User via User And Password.

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
        response = requests.request("POST", url=self.url, headers=self.headers_user_pwd, data=data,
                                    auth=HTTPBasicAuth(username=self.user, password=self.password))
        return self._logger_response(response)
