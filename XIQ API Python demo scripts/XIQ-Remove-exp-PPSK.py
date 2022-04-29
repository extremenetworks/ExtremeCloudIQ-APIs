import requests
import json
import getpass
from datetime import datetime
from time import mktime
import os
import logging

#-------------------------
# logging
PATH = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(
    filename='{}/XIQ-PPSK-remove.log'.format(PATH),
    filemode='a',
    level=os.environ.get("LOGLEVEL", "INFO"),
    format= '%(asctime)s: %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'
)


URL = "https://api.extremecloudiq.com"

print(" ExtremeCloudIQ - remove expired PPSK users -  Builder v1.0")
print()
print("Enter your ExtremeCloudIQ login credentials")
username = input ("Email: ")
password = getpass.getpass("Password: ")


headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}


# login and request access token
def GetaccessToken(username,password):
    url = URL + "/login"
    payload = json.dumps({"username": username, "password": password})
    response = requests.post(url, headers=headers, data=payload)
    if response is None:
        print("ERROR: Not able to login into ExtremeCloudIQ - no response!")

        return -1
    if response.status_code != 200:
        print("ERROR: Not able to login into XIQ - HTTP Status Code: " +
              str(response.status_code))
        print(response)
        return -2
    data = response.json()

    if 'access_token' in data:
        print("\nLogged in and Got access token: " + data['access_token'])
        headers["Authorization"] = "Bearer " + data['access_token']
        return 0

    else:
        return -3

def retrievePPSKusers(pageSize):
    print("Retrieving all PPSK users from ExtremeCloudIQ")
    page = 1

    ppskusers = []

    while page < 1000:
        url = URL + "/endusers?page=" + str(page) + "&limit=" + str(pageSize)
       # print("Retrieving next page of PPSK users from ExtremeCloudIQ starting at page " +
          #    str(page) + " url: " + url)

        # Get the next page of the ppsk users
        response = requests.get(url, headers=headers, verify = True)
        if response is None:
            print("Error retrieving PPSK users from XIQ - no response!")
            return

        if response.status_code != 200:
            print("Error retrieving PPSK users from XIQ - HTTP Status Code: " +
                  str(response.status_code))
            print(response)
            return

        rawList = response.json()['data']
        for name in rawList:
            print(name)
        print("Retrieved " + str(len(rawList)) +
              " users on this page")
        log_msg = [name]
        logging.error(log_msg)
        ppskusers = ppskusers + rawList

        if len(rawList) == 0:
            print("\nReached the final page - stopping to retrieve users ")
            break

        page = page + 1

    return ppskusers


def removeuser(userID):
    url = URL + "/endusers/" + str(userID)
    print("\nTrying to delete user using this URL and payload\n " + url)
    response = requests.delete(url, headers=headers, verify=True)
    if response is None:
        print("\nError deleting PPSK user - no response!")
        return
    if response.status_code != 200:
        print("\nError deleting PPSK user - HTTP Status Code:\n" +
              str(response.status_code))
        print(response)
        return
    if response.status_code == 200:
        print("\nsuccesfully deleted PPSK user\n")
        log_msg = f"\nsucessfully deleted PPSK user"
        logging.error(log_msg)
    print(response)
    log_msg2 =(response)
    logging.error(log_msg2)


# current date and time


dt = datetime.now()
print("all users expired on " + str(dt) + " will be removed")
sec_since_epoch = mktime(dt.timetuple())

timestamp = sec_since_epoch * 1000


print("timestamp = " + str(timestamp))

#main

try:
    login = GetaccessToken(username,password)
except TypeError as e:
    print(e)
    raise SystemExit
except:
    print("Unknown Error: Failed to generate token")
    raise SystemExit

ppskuser = retrievePPSKusers(10)
userID = 0
for user in ppskuser:
    if user['expired_time'] < timestamp:
        userID = user['id']
        username = user['user_name']
        print("\nFound expired user id: " + str(username) + " " + str(userID) + \
              " --> trying to delete this user")
        log_msg = f"\nFound expired user id: " + str(username) + " " + str(userID) + \
              " --> trying to delete this user"
        logging.error(log_msg)

        remove=removeuser(userID)

if userID == 0:
    print("\nNo users removed")
    log_msg = f"\nNo users removed"
    logging.error(log_msg)
