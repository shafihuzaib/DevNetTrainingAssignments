
#Assignment 1

1. Fork this repository
2. Clone the fork onto your local dev
3. Create a script, that parses db files in data directory
4. Show information from all accounts ACT100 to ACT900 on the console
5. Create another script to parse data in dnac_devices.json
6. For each device, show the following:
      id, type, family, softwareType, managementIpAddress
7. Capture a screenshot of the output 
8. Push changes to your fork

Notes: 
1. Each script should have it's own commit. There can be more than two commits.
2. Create a branch named assignment1 to solve this problem and push commits to it.
3. Unit Tests are mandatory (TDD is recommended)


##Assignment 2

APIs

POST https://sandboxdnac2.cisco.com/api/system/v1/auth/token
HTTP Basic (dnacdev / D3v93T@wK!)

GET https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device
x-auth-token header 


1. Create a new branch from assignment1 branch, that you created earlier
2. Adapt the dnac devices script to get data from the above API
3. Modularize the code as much as possible
