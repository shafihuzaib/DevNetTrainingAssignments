
# Assignment 1

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


# Assignment 2

APIs

POST https://sandboxdnac2.cisco.com/api/system/v1/auth/token
HTTP Basic (dnacdev / D3v93T@wK!)

GET https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device
x-auth-token header 


1. Create a new branch from assignment1 branch, that you created earlier
2. Adapt the dnac devices script to get data from the above API
3. Modularize the code as much as possible


# Assignment 3

Notes: `<image_name>, <script>, <host_port>` and such variables in `commands` and inside `docker-compose.yml` are left for a value to be decided by the developer. So assign appropriate values before running and code commit.

1. Create a new branch from assignment2 branch
2. Copy the Dockerfile, docker-compose.yml, requirements.txt and index.py from this repository's master
3. Adapt existing scripts like index.py, so that they can be executed as CGI Scripts
4. Go for following Docker tasks (.. and experiment with more):
      - Using `docker build -t <image_name> .` build a docker image
      - Using `docker run -p <host_port>:80 <image_name>` run the docker image
      - Check in your browser the output of your scripts `http://localhost:<host_port>/<script>.py`
      - Using `docker container ls`, check the running status of the containers
      - Using `docker stop <container_id>` stop the container
      - Using `docker-compose up` bring up the containers again
      - Check the scripts in the browser again
      - Using `docker-compose down` stop the containers
5. For Development Environment, use `-v` property with `docker run`
      - Also review `volumes` section in `docker-compose.yml`

### Deliverables of this assignment
      - New script files, which can run as cgi-scripts
      - Updated docker-compose.yml
      - A text file, which contains the exact commands you executed in our local environment
