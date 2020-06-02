import dnac
from pprint import pprint 
token = dnac.gettoken('https://sandboxdnac2.cisco.com/api/system/v1/auth/token','ZG5hY2RldjpEM3Y5M1RAd0sh')
data=dnac.getdev('https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device',token)
pprint(data)