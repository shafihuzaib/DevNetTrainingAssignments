import json
import yaml
import xmltodict
import xml.etree.ElementTree as ET
from pprint import pprint

li=[]
with open("data/db.json") as dbj:
    #print(dbj)
    
    datajs= json.load(dbj)
    li.append(datajs)
    

with open("data/db.xml") as dbx:
    dataxm = json.loads(json.dumps((xmltodict.parse(dbx.read(),process_namespaces=True))))
    li.append(dataxm["root"])

with open("data/db.yml") as dbym:
    dataym = yaml.safe_load(dbym)
    li.append(dataym)

for i in li:
    pprint(i, indent=4)
    