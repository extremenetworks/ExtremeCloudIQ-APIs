import json
from typing import Type
import requests
import secrets
import string
import sys
import time
import os
import logging


# setup your settings

server_name = "enter your server name or IP"
domain_name = "enter you domain name"
user_name = "enter your username"
password = "enter your password"
XIQ_username = "enter your ExtremeCloudIQ Username"
XIQ_password = "enter your ExtremeCLoudIQ password
usergroupID = " enter your user group ID"

#-------------------------
# logging
PATH = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(
    filename='{}/XIQ-AD-PPSK-sync.log'.format(PATH),
    filemode='a',
    level=os.environ.get("LOGLEVEL", "INFO"),
    format= '%(asctime)s: %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'
)


URL = "https://api.extremecloudiq.com"
headers = {"Accept": "application/json", "Content-Type": "application/json"}

from ldap3 import Server, Connection, ALL, NTLM, ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES, AUTO_BIND_NO_TLS, SUBTREE



try:
    server = Server(server_name, get_info=ALL)
    conn = Connection(server, user='{}\\{}'.format(domain_name, user_name), password=password, authentication=NTLM, auto_bind=True)
    conn.search('dc={},dc=local,'.format(domain_name), '(objectclass=person)', attributes=['name', 'mail', 'userAccountControl'])
except:
    log_msg = f"Unable to reach server {server_name}"
    logging.error(log_msg)
    print(log_msg)
    print("script exiting....")
    # not having ppsk will break later line - for ldap_entry in conn.entries:
    raise SystemExit



def GetaccessToken(XIQ_username, XIQ_password):
    url = URL + "/login"
    payload = json.dumps({"username": XIQ_username, "password": XIQ_password})
    response = requests.post(url, headers=headers, data=payload)
    if response is None:
        log_msg = "ERROR: Not able to login into ExtremeCloudIQ - no response!"
        logging.error(log_msg)
        raise TypeError(log_msg)
    if response.status_code != 200:
        log_msg = f"Error getting access token - HTTP Status Code: {str(response.status_code)}"
        logging.error(f"{log_msg}")
        logging.warning(f"\t\t{response}")
        raise TypeError(log_msg)
    data = response.json()

    if "access_token" in data:
        #print("Logged in and Got access token: " + data["access_token"])
        headers["Authorization"] = "Bearer " + data["access_token"]
        return 0

    else:
        log_msg = "Unknown Error: Unable to gain access token"
        logging.warning(log_msg)
        raise TypeError(log_msg)


def CreatePPSKuser(name,mail):
    url = URL + "/ssids/users"

    payload = json.dumps({"user_group_id": usergroupID ,"name": name,"user_name": name,"password": "", "email_address": mail, "email_password_delivery": mail})

    #print("Trying to create user using this URL and payload " + url)
    response = requests.post(url, headers=headers, data=payload, verify=True)
    if response is None:
        log_msg = "Error adding PPSK user - no response!"
        logging.error(log_msg)
        raise TypeError(log_msg)

    elif response.status_code != 200:
        log_msg = f"Error adding PPSK user {name} - HTTP Status Code: {str(response.status_code)}"
        logging.error(log_msg)
        logging.warning(f"\t\t{response}")
        raise TypeError(log_msg)

    elif response.status_code ==200:
        logging.info(f"succesfully created PPSK user {name}")
        print(f"succesfully created PPSK user {name}")
    #print(response)




def retrievePPSKusers(pageSize):
    #print("Retrieve all PPSK users  from ExtremeCloudIQ")
    page = 1

    ppskusers = []

    while page < 1000:
        url = URL + "/ssids/users?page=" + str(page) + "&limit=" + str(pageSize)
        #print("Retrieving next page of PPSK users from ExtremeCloudIQ starting at page " + str(page) + " url: " + url)

        # Get the next page of the ppsk users
        response = requests.get(url, headers=headers, verify = True)
        if response is None:
            log_msg = "Error retrieving PPSK users from XIQ - no response!"
            logging.error(log_msg)
            raise TypeError(log_msg)

        elif response.status_code != 200:
            log_msg = f"Error retrieving PPSK users from XIQ - HTTP Status Code: {str(response.status_code)}"
            logging.error(f"Error retrieving PPSK users from XIQ - HTTP Status Code: {str(response.status_code)}")
            logging.warning(f"\t\t{response}")
            raise TypeError(log_msg)


        rawList = response.json()['data']
        #for name in rawList:
        #    print(name)
        #print("Retrieved " + str(len(rawList)) + " users on this page")
        ppskusers = ppskusers + rawList

        if len(rawList) == 0:
            #print("Reached the final page - stopping to retrieve users ")
            break

        page = page + 1
        return ppskusers



def deleteuser(userId):
    url = URL + "/ssids/users/" + str(userId)
    #print("\nTrying to delete user using this URL and payload\n " + url)
    response = requests.delete(url, headers=headers, verify=True)
    if response is None:
        log_msg = f"Error deleting PPSK user {userId} - no response!"
        logging.error(log_msg)
        raise TypeError(log_msg)
    elif response.status_code != 200:
        log_msg = f"Error deleting PPSK user {userId} - HTTP Status Code: {str(response.status_code)}"
        logging.error(log_msg)
        logging.warning(f"\t\t{response}")
        raise TypeError(log_msg)
    elif response.status_code == 200:
        logging.info(f"succesfully deleted PPSK user {userId}")
        print(f"succesfully deleted PPSK user {userId}")
    #print(response)

# MAIN
try:
    login = GetaccessToken(XIQ_username, XIQ_password)
except TypeError as e:
    print(e)
    raise SystemExit
except:
    log_msg = "Unknown Error: Failed to generate token"
    logging.error(log_msg)
    print(log_msg)
    raise SystemExit

try:
    ppsk_users = retrievePPSKusers(100)
except TypeError as e:
    print(e)
    print("script exiting....")
    # not having ppsk will break later line - if not any(d['name'] == name for d in ppsk_users):
    raise SystemExit
except:
    log_msg = ("Unknown Error: Failed to retrieve users from XIQ")
    logging.error(log_msg)
    print(log_msg)
    print("script exiting....")
    # not having ppsk will break later line - if not any(d['name'] == name for d in ppsk_users):
    raise SystemExit

ldap_users = {}

#print("\nParsing all users from LDAP:\n")
#print(conn.entries)

for ldap_entry in conn.entries:
    try:
        ldap_users[str(ldap_entry.name)] = {
            "userAccountControl": str(ldap_entry.userAccountControl),
            "email": str(ldap_entry.mail)}

    except:
        log_msg = (f"Unexpected error: {sys.exc_info()[0]}")
        logging.error(log_msg)
        print(log_msg)
        print("script exiting....")
        # not having ppsk will break later line - for name, details in ldap_users.items():
        raise SystemExit


#print("\nSuccessfully parsed " + str(len(ldap_users)) + " LDAP users\n")

for name, details in ldap_users.items():
    if not any(d['name'] == name for d in ppsk_users):
        try:
            CreatePPSKuser(name, details["email"])
        except TypeError as e:
            print(e)
        except:
            log_msg = f"Unknown Error: Failed to create user {name}"
            logging.error(log_msg)
            print(log_msg)

    #print("Check account " + name + ": userAccountControl: " + details["userAccountControl"])

    if details["userAccountControl"] == '66050':

        userId=0
        for user in ppsk_users:
            if user['name'] == name:
                userId=user['id']
                #print("Found user id: " + str(userId) + " --> trying to delete this user")
                deletePPSKuser=deleteuser(userId)
                break

        if userId == 0:
            log_msg = (f"Failed to retrieve data on user by username {name}")
            logging.error(log_msg)
            print(log_msg)





