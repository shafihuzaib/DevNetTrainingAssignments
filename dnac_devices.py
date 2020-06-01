import json
from pprint import pprint
li=[]
with open("data/dnac_devices.json") as dnc:
    data = json.load(dnc)
    for d in data["response"]:
        temp = {}
        temp['id'] = d['id']
        temp['family'] = d['family']
        temp['softwareType'] = d['softwareType']
        temp['type'] = d['type']
        temp['managementIpAddress'] = d['managementIpAddress']
        pprint(temp, indent=4)
