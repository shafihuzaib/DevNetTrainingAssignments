import json
from data import parse_json
from get_dnac import get_file

def dev_par(u_name,p_word,site1,site2):
    dev_data = get_file(u_name,p_word,site1,site2)
    for dnac_device in dev_data['response']:
            print('\nDevice ID :', dnac_device['id'])
            print('Device Type :', dnac_device['type'])
            print('Device Family :', dnac_device['family'])
            print('Software Type :', dnac_device['softwareType'])
            print('Management IP Address :', dnac_device['managementIpAddress'],'\n')


if __name__ =='__main__':
    # Iterating through all files in data directory:
    print('\nDevice Details : ')
    print('-------------------\n')
    site1 = 'https://sandboxdnac2.cisco.com/api/system/v1/auth/token'
    site2 = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device'
    un: str = input("Enter username : ")
    ps: str = input("Enter password : ")

    dev_par(un,ps,site1,site2)