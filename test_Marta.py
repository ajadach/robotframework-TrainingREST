import requests
import json


def logger_response_postive(response):
    print('=== RESPONSE ===')
    print("Headers:", json.dumps(dict(response.headers), indent=4))

    try:
        print("Body:", json.dumps(response.json(), indent=2))
    except Exception:
        pass

    print("Status Code:", response.status_code, '\n')
    if response.status_code not in [200, 201, 202, 204]:
        raise ValueError("Wrong Status Code")


def logger_response_negative(response):
    print('=== RESPONSE ===')
    print("Headers:", json.dumps(dict(response.headers), indent=4))

    try:
        print("Body:", json.dumps(response.json(), indent=2))
    except Exception:
        pass

    print("Status Code:", response.status_code, '\n')
    if response.status_code not in [400, 201, 402, 404]:
        raise ValueError("Wrong Status Code")


""" GLOBAL VARS """
TOKEN = '77fc5fa2cc6fa7336bd3db9afb9be6f924cbe322bb5fc438864287c0359bdd08'
URL = 'https://gorest.co.in/public/v2/users'
HEADERS = {
    "Authorization": f'Bearer {TOKEN}',
    "Accept": "application/json",
}


# CREATE MULTI USERS

for i in range(2):
    file_name = f'data/{i}.json'
    with open(file_name, "r") as file:
        body = json.load(file)

    response = requests.request("POST", url=URL, headers=HEADERS, data=body)
    logger_response_postive(response)
