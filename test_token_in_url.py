import requests
import json


def logger_reponse(response):
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
URL_TOKEN = f'{URL}?access-token={TOKEN}'
URL_PATCH = '{}/{}?access-token={}'


"""
curl -i -H "Accept:application/json" -H "Content-Type:application/json" 
-H "Authorization: Bearer 77fc5fa2cc6fa7336bd3db9afb9be6f924cbe322bb5fc438864287c0359bdd08" 
-XGET "https://gorest.co.in/public/v2/users"
"""
# response = requests.request("GET", url=URL_TOKEN, headers={}, data={})


"""
curl -i -H "Accept:application/json" -H "Content-Type:application/json" 
-H "Authorization: Bearer 77fc5fa2cc6fa7336bd3db9afb9be6f924cbe322bb5fc438864287c0359bdd08" 
-XPOST "https://gorest.co.in/public/v2/users" 
-d '{"name":"Tenali Ramakrishna", "gender":"male", "email":"tenali.ramakrishna@15ce.com", "status":"active"}'
"""

body = {
    "name": "asdas",
    "gender": "male",
    "email": "qweqwe@wwwww",
    "status": "active"
}

# response = requests.request("POST", url=URL_TOKEN, headers={}, data=body)
# logger_reponse(response)
# assert response.json()['id']


"""
curl -i -H "Accept:application/json" -H "Content-Type:application/json" 
-H "Authorization: Bearer 77fc5fa2cc6fa7336bd3db9afb9be6f924cbe322bb5fc438864287c0359bdd08" 
-XPATCH "https://gorest.co.in/public/v2/users/2139418" 
-d '{"name":"Allasani Peddana", "email":"allasani.peddana@15ce.com", "status":"active"}'
"""

# TU TRZEBA PODAC ID KTORE ISTNIEJE, ID MOZNA ZOBACZYC W GET
# ID = '6850433'
#
# body = {
#     "email": "qweqwe@wwwww",
# }
#
# response = requests.request("PATCH", url=URL_PATCH.format(URL, ID, TOKEN), headers={}, data=body)
# logger_reponse(response)
# assert response.json()['id']

"""
curl -i -H "Accept:application/json" -H "Content-Type:application/json" 
-H "Authorization: Bearer 77fc5fa2cc6fa7336bd3db9afb9be6f924cbe322bb5fc438864287c0359bdd08" 
-XDELETE "https://gorest.co.in/public/v2/users/2139418"
"""

# TU TRZEBA PODAC ID KTORE NIE JEST USUNIETE, ID MOZNA ZOBACZYC W GET
ID = '6850433'

response = requests.request("DELETE", url=URL_PATCH.format(URL, ID, TOKEN), headers={}, data={})
logger_reponse(response)
assert response.json()['id']
