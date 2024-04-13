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


# Authorization: Bearer 77fc5fa2cc6fa7336bd3db9afb9be6f924cbe322bb5fc438864287c0359bdd08
HEADERS = {
    "Authorization": f'Bearer {TOKEN}',
    "Accept": "application/json",
}

"""
curl -i -H "Accept:application/json" -H "Content-Type:application/json" 
-H "Authorization: Bearer 77fc5fa2cc6fa7336bd3db9afb9be6f924cbe322bb5fc438864287c0359bdd08" 
-XGET "https://gorest.co.in/public/v2/users"
"""
#
# response = requests.request("GET", url=URL, headers=HEADERS, data={})
# logger_reponse(response)
#

"""
curl -i -H "Accept:application/json" -H "Content-Type:application/json" 
-H "Authorization: Bearer 77fc5fa2cc6fa7336bd3db9afb9be6f924cbe322bb5fc438864287c0359bdd08" 
-XPOST "https://gorest.co.in/public/v2/users" 
-d '{"name":"Tenali Ramakrishna", "gender":"male", "email":"tenali.ramakrishna@15ce.com", "status":"active"}'
"""

body = {
    "name": "asdas",
    "gender": "male",
    "email": "q2w22eq2we@ww2wwww",
    "status": "active"
}
#
# response = requests.request("POST", url=URL, headers=HEADERS, data=body)
# logger_reponse(response)
#

"""
curl -i -H "Accept:application/json" -H "Content-Type:application/json" 
-H "Authorization: Bearer 77fc5fa2cc6fa7336bd3db9afb9be6f924cbe322bb5fc438864287c0359bdd08" 
-XPATCH "https://gorest.co.in/public/v2/users/2139421" -d '{"name":"Allasani Peddana", "email":"allasani.peddana@15ce.com", "status":"active"}'
"""

ID = '6850519'

body = {
    "email": "q2wasd22eq2we@ww2wwww",
}
#
# response = requests.request("PATCH", url=URL+f'/{ID}', headers=HEADERS, data=body)
# logger_reponse(response)

"""
curl -i -H "Accept:application/json" -H "Content-Type:application/json" 
-H "Authorization: Bearer 77fc5fa2cc6fa7336bd3db9afb9be6f924cbe322bb5fc438864287c0359bdd08" 
-XDELETE "https://gorest.co.in/public/v2/users/2139421"
"""

ID = '6850519'
#
# response = requests.request("DELETE", url=URL+f'/{ID}', headers=HEADERS, data={})
# logger_reponse(response)
