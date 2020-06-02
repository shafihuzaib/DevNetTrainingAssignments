
from ruamel import yaml

import os
import json
import xml.etree.ElementTree as ET 
    
def parse_yaml():
    with open('C:/Users/thsindhu/Documents/GitHub/DevNetTrainingAssignments/data/db.yml', 'r') as yaml_file:
        db_yaml = yaml.safe_load(yaml_file)
        parse_data = db_yaml
        print(parse_data)
    
def parse_json():
    with open('C:/Users/thsindhu/Documents/GitHub/DevNetTrainingAssignments/data/db.json','r') as json_file :
        db_json = json.load(json_file)
        parse_data = db_json
        print(parse_data)

def parse_xml():
    with open('C:/Users/thsindhu/Documents/GitHub/DevNetTrainingAssignments/data/db.xml','r') as xml_file :
        tree = ET.parse(xml_file) 

        root = tree.getroot() 
        accounts = [] 

        for accounts in root: #iterate all the roots
           print(accounts.tag, accounts.attrib)
           print(":")
           for account_amt in accounts : #iterate all the chidren
               print('\t',account_amt.tag,int(account_amt.text))

parse_json()

parse_xml()

parse_yaml()

