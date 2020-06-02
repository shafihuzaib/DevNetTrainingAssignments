import requests,json

def gettoken(url,usrpwd):
    payload = {}
    headers = {
      'Authorization': 'Basic {}'.format(usrpwd)}
    response = requests.request("POST", url, headers=headers, data = payload)
    token=(response.json())['Token']
    return(token)

def getdev(url,token):
    payload={}
    headers={'x-auth-token' : token}
    response = requests.request("GET", url, headers=headers, data = payload)
    return (response.json())['response']

    

