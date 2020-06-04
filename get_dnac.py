import requests
import json

def get_file(usernam,passwor,site1,site2):
    url = site1

    payload = {}
    headers = {
        'Authorization': 'Basic ZG5hY2RldjpEM3Y5M1RAd0sh'
    }

    response = requests.request("POST", url, headers=headers, data = payload)

    resp = json.loads(response.text.encode('utf8'))

    token = resp["Token"]

    url = site2

    payload = {}
    headers = {
        'x-auth-token': token
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    resp1 = json.loads(response.text.encode('utf8'))

    return(resp1)