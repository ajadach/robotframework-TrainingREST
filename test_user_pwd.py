import requests
import json

from requests.auth import HTTPBasicAuth

def logger_response(response):
    print('=== RESPONSE ===')
    print("Headers:", json.dumps(dict(response.headers), indent=4))

    try:
        print("Body:", json.dumps(response.json(), indent=2))
    except Exception:
        pass

    print("Status Code:", response.status_code, '\n')
    if response.status_code not in [200, 201, 202, 204]:
        raise ValueError("Wrong Status Code")


""" GLOBAL VARS """
TOKEN = '77fc5fa2cc6fa7336bd3db9afb9be6f924cbe322bb5fc438864287c0359bdd08'
URL = 'https://gorest.co.in/public/v2/users'

# Authorization: Bearer 77fc5fa2cc6fa7336bd3db9afb9be6f924cbe322bb5fc438864287c0359bdd08
HEADERS = {
    "Accept": "application/json",
}

USER = 'admin'
PWD = 'password'

response = requests.request("GET", url=URL, headers=HEADERS, auth=HTTPBasicAuth(username=USER, password=PWD))
logger_response(response)
#
# body = {
#     "name": "asdas",
#     "gender": "male",
#     "email": "qweq123114we@wwwww",
#     "status": "active"
# }
#
# response = requests.request("POST", url=URL, headers=HEADERS, auth=HTTPBasicAuth(username=TOKEN, password=''), data=body)
# logger_response(response)
