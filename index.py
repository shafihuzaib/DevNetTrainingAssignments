#!/usr/bin/python3
print("Content-Type:text/html")
print("")

import cgi,cgitb
cgitb.enable() # Enable debugging
print("<h1>Below is the execution output of the script</h1>")
print("------------------------------------<br>")

##-------PASTE YOUR SCRIPT BELOW---------#######

import requests


def get_token():
    """
    Gets an access token from Cisco DNA Center. Returns the token
    string if successful; raises HTTPError otherwise.
    """

    # Declare useful local variables to simplify request process
    api_path = "https://sandboxdnac2.cisco.com/dna"
    auth = ("dnacdev", "D3v93T@wK!")
    headers = {"Content-Type": "application/json"}

    # Issue HTTP POST request to the proper URL to request a token
    auth_resp = requests.post(
        "{}/system/api/v1/auth/token".format(api_path), auth=auth, headers=headers
    )

    # If successful, print token. Else, raise HTTPError with details
    auth_resp.raise_for_status()
    token = auth_resp.json()["Token"]
    return token


def main():
    """
    Execution begins here.
    """

    print("<h3>Printing Token...</h3>")
    token = get_token()
    print("<h3>Token</h3><br><br>{}".format(token) )
    print("<h3>Token printed</h3>")

main()