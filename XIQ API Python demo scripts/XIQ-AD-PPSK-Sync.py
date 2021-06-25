import json
from typing import Type
import requests
import secrets
import string
import sys
import time
import os
import logging


# Global Variables - ADD CORRECT VALUES
server_name = "enter your server name or IP"
domain_name = "enter you domain name"
user_name = "enter your username"
password = "enter your password"
ad_group = "enter active directory group"
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
# userAccountControl codes used for disabled accounts
ldap_disable_codes = ['514','66050']

URL = "https://api.extremecloudiq.com"
headers = {"Accept": "application/json", "Content-Type": "application/json"}

from ldap3 import Server, Connection, ALL, NTLM, ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES, AUTO_BIND_NO_TLS, SUBTREE



def retrieveADUsers(ad_group):
    #Building search base from fqdn
    subdir_list = fqdn.split('.')
    tdl = subdir_list[-1]
    subdir_list = subdir_list[:-1]
    SearchBase = 'DC=' + ',DC='.join(subdir_list) + ',DC=' + tdl
    try:
        server = Server(server_name, get_info=ALL)
        conn = Connection(server, user='{}\\{}'.format(domain_name, user_name), password=password, authentication=NTLM, auto_bind=True)
        conn.search(
                search_base= SearchBase,
                search_filter='(&(objectClass=user)(memberof:1.2.840.113556.1.4.1941:=cn={},cn=users,{}))'.format(ad_group, SearchBase),
                search_scope=SUBTREE,
                attributes = ['objectClass', 'userAccountControl', 'sAMAccountName', 'name', 'mail'])
        ad_result = conn.entries
        conn.unbind()
        return ad_result
    except:
        log_msg = f"Unable to reach server {server_name}"
        logging.error(log_msg)
        print(log_msg)
        print("script exiting....")
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
        url = URL + "/ssids/users?page=" + str(page) + "&limit=" + str(pageSize) + "&user_group_ids=" + usergroupID
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
        return 'Success'
    #print(response)

def main():
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
    ldap_capture_success = True
    ad_result = retrieveADUsers(ad_group)
    #print("\nParsing all users from LDAP:\n")

    for ldap_entry in ad_result:
        if str(ldap_entry.name) not in ldap_users:
            try:
                ldap_users[str(ldap_entry.name)] = {
                    "userAccountControl": str(ldap_entry.userAccountControl),
                    "email": str(ldap_entry.mail)}

            except:
                log_msg = (f"Unexpected error: {sys.exc_info()[0]}")
                logging.error(log_msg)
                print(log_msg)
                logging.warning("User info was not captured from Active Directory")
                logging.warning(f"{ldap_entry}")
                # not having ppsk will break later line - for name, details in ldap_users.items():
                ldap_capture_success = False
                continue


    log_msg = "Successfully parsed " + str(len(ldap_users)) + " LDAP users"
    logging.info(log_msg)
    #print(f"\n{log_msg}\n")

    ldap_disabled = []
    for name, details in ldap_users.items():
        if details['email'] == '[]':
            print(f"User {name} doesn't have a email set")
            continue
        if not any(d['name'] == name for d in ppsk_users) and not any(d == details['userAccountControl'] for d in ldap_disable_codes):
            try:
                CreatePPSKuser(name, details["email"])
            except TypeError as e:
                log_msg = f"failed to create {name}: {e}"
                logging.error(log_msg)
                print(log_msg)
            except:
                log_msg = f"Unknown Error: Failed to create user {name}"
                logging.error(log_msg)
                print(log_msg)
        elif any(d == details['userAccountControl'] for d in ldap_disable_codes):
            ldap_disabled.append(name)
    
    # Remove disabled accounts from ldap users
    for name in ldap_disabled:
        del ldap_users[name]
    if ldap_capture_success:
        for x in ppsk_users:
            email = x['email_address']
            xiqid = x['id']
            # check if any xiq user is not included in active ldap users
            if not any(d['email'] == email for d in ldap_users.values()):
                try:
                    result = deleteuser(xiqid)
                except TypeError as e:
                    logmsg = f"Failed to delete user {email}  with error {e}"
                    logging.error(logmsg)
                    print(logmsg)
                    continue
                except:
                    log_msg = f"Unknown Error: Failed to create user {email} "
                    logging.error(log_msg)
                    print(log_msg)
                    continue
                if result == 'Success':
                    log_msg = f"User {email} was successfully deleted."
                    logging.info(log_msg)
                    print(log_msg)  
    else:
        log_msg = "No users will be deleted from XIQ because of the error(s) in reading ldap users"
        logging.warning(log_msg)
        print(log_msg)


if __name__ == '__main__':
	main()
