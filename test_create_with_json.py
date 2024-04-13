import requests
import json


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
HEADERS = {
    "Authorization": f'Bearer {TOKEN}',
    "Accept": "application/json",
}


"""
curl -i -H "Accept:application/json" -H "Content-Type:application/json" 
-H "Authorization: Bearer 77fc5fa2cc6fa7336bd3db9afb9be6f924cbe322bb5fc438864287c0359bdd08" 
-XPOST "https://gorest.co.in/public/v2/users" 
-d '{"name":"Tenali Ramakrishna", "gender":"male", "email":"tenali.ramakrishna@15ce.com", "status":"active"}'
"""

# CREATE MULTI USERS

# file_name = 'user_data_1.json'
# with open(file_name, "r") as file:
#     body = json.load(file)
#
# for user in body:
#     response = requests.request("POST", url=URL, headers=HEADERS, data=user)
#     logger_response(response)


"""
curl -i -H "Accept:application/json" -H "Content-Type:application/json" 
-H "Authorization: Bearer 77fc5fa2cc6fa7336bd3db9afb9be6f924cbe322bb5fc438864287c0359bdd08" 
-XPATCH "https://gorest.co.in/public/v2/users/2139421" 
-d '{"name":"Allasani Peddana", "email":"allasani.peddana@15ce.com", "status":"active"}'
"""

# UPDATE MULTI USERS
# file_name = 'user_data_2_update.json'
# with open(file_name, "r") as file:
#     body = json.load(file)
#
# for user in body:
#     id = user.pop('id')
#     response = requests.request("PATCH", url=URL+f'/{id}', headers=HEADERS, data=user)
#     logger_response(response)


"""
curl -i -H "Accept:application/json" -H "Content-Type:application/json" 
-H "Authorization: Bearer 77fc5fa2cc6fa7336bd3db9afb9be6f924cbe322bb5fc438864287c0359bdd08" 
-XDELETE "https://gorest.co.in/public/v2/users/2139421"
"""
# DELETE MULTI USERS
file_name = 'user_data_2_update.json'
with open(file_name, "r") as file:
    body = json.load(file)

for user in body:
    id = user.pop('id')
    response = requests.request("DELETE", url=URL+f'/{id}', headers=HEADERS, data={})
    logger_response(response)
