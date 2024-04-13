import requests
import json

from requests.auth import HTTPBasicAuth


class driver_live:
    """Driver live coding."""

    def __init__(self):
        self.token = ''
        self.url = 'https://gorest.co.in/public/v2/users'
        self.headers = ''

    def generate_token(self, user, password):
        """ Generate Token.

         *Arguments:*
         | =Name= | =Description= | =Example value= |
         | user | user name | admin |
         | password | password name | pwd123 |

         *Return*
         | string | token value base on user and password |
         """
        # token = requests.request("GET", url=URL, headers=HEADERS, auth=HTTPBasicAuth(username=USER, password=PWD))

        self.token = '77fc5fa2cc6fa7336bd3db9afb9be6f924cbe322bb5fc438864287c0359bdd08'
        self.headers = {
            "Authorization": f'Bearer {self.token}',
            "Accept": "application/json",
        }
        return self.token

    def get(self, id_user=None):
        """ Get for users.

         *Arguments:*
         | =Name= | =Description= | =Example value= |
         | id_user | id for user, defautl None | 2137896 |

         *Return*
         | dict | data for users or user |
         """
        if id_user:
            new_url = self.url + f'/{id_user}'
        else:
            new_url = self.url

        response = requests.request("GET", url=new_url, headers=self.headers, data={})
        return self._logger_reponse(response)

    # def post(self, name, gender, email, status):
    #     body = {
    #         "name": name,
    #         "gender": gender,
    #         "email": email,
    #         "status": status
    #     }
    def post(self, **kwargs):
        """ Get for users.

         *Arguments:*
         | =Name= | =Description= | =Example value= |
         | name | id for user, defautl None | 2137896 |
         | email | id for user, defautl None | 2137896 |
         | ... | id for user, defautl None | 2137896 |

         *Return*
         | dict | data for users or user |
         """
        # TODO: sprawdzic czy wszystkie key sa
        response = requests.request("POST", url=self.url, headers=self.headers, data=kwargs)
        assert response['id']
        return self._logger_reponse(response)

    def patch(self, id_user, **kwargs):
        """ Update for users.

         *Arguments:*
         | =Name= | =Description= | =Example value= |
         | id_user | id for user | 2137896 |
         | name | id for user, defautl None | 2137896 |
         | email | id for user, defautl None | 2137896 |
         | ... | id for user, defautl None | 2137896 |

         *Return*
         | dict | data for users or user |
         """
        response = requests.request("PATCH", url=self.url + f'/{id_user}', headers=self.headers, data=kwargs)
        assert response['id']
        return self._logger_reponse(response)

    def delete(self, id_user):
        """ Delete for user.

         *Arguments:*
         | =Name= | =Description= | =Example value= |
         | id_user | id for user | 2137896 |

         *Return*
         | dict | data for users or user |
         """
        response = requests.request("DELETE", url=self.url + f'/{id_user}', headers=self.headers, data={})
        return self._logger_reponse(response)

    def _logger_reponse(self, response):
        print('=== RESPONSE ===')
        print("Headers:", json.dumps(dict(response.headers), indent=4))

        try:
            print("Body:", json.dumps(response.json(), indent=2))
        except Exception:
            pass

        print("Status Code:", response.status_code, '\n')
        if response.status_code not in [200, 201, 202, 204]:
            raise ValueError("Wrong Status Code")
