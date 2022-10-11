import requests
import json
import logging
import getpass
import random
import string
import datetime

URL = "https://api.extremecloudiq.com"

print(" ExtremeCloudIQ - Create PPSK user -  Builder v1.0")
print()
print("Enter your ExtremeCloudIQ login credentials")
username = input ("Email: ")
password = getpass.getpass("Password: ")
logger = logging.getLogger()

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
        print("Logged in and Got access token: " + data['access_token'])
        headers["Authorization"] = "Bearer " + data['access_token']
        return 0

    else:
        return -3

# List all UserGroups
def listusergroups(pageSize):
    print("list all user groups from XIQ with page size of " + str(pageSize))
    page = 1
    allgroups = []

    while page < 1000:
        url = URL + "/usergroups?page=" + str(page) + "&limit=" + str(pageSize)
        print("Retrieving next page of user groups from XIQ starting at page " +
              str(page) + " url: " + url)

        # Get the next page of user groups
        response = requests.get(url, headers=headers, verify = True)
        if response is None:
            print("Error retrieving user groups from XIQ - no response!")
            return

        if response.status_code != 200:
            print("Error retrieving user groups from XIQ - HTTP Status Code: " +
                  str(response.status_code))
            print(response)
            return

        rawList = response.json()['data']
        for name in rawList:
            print(name)
        print("Retrieved " + str(len(rawList)) +
              " user groups on this page")
        allgroups = allgroups + rawList

        if len(rawList) == 0:
            print("Reached the final page - stopping to retrieve user groups")
            break

        page = page + 1

    return allgroups

# Create PPSK user

def CreatePPSKuser(usergroupId,name1,user_name):
    filename1 = "PPSK_" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    url = URL + "/endusers"

    payload = json.dumps({"user_group_id": usergroupId,"name": name1,"user_name": user_name,"password": "", "email_address": email_address, "email_password_delivery": email_address})

    print("Trying to create user using this URL and payload " + url)
    print(payload, file=open(filename1 + ".txt" , "a"))
    response = requests.post(url, headers=headers, data=payload, verify=True)
    if response is None:
        print("Error adding PPSK user - no response!")
        return

    if response.status_code != 200:
        print("Error adding PPSK user - HTTP Status Code: " +
              str(response.status_code))
        print(response.text)
        print(response)
        return

    print(response.content)

# list all PPSK users

def retrievePPSKusers(pageSize):
    print("Retrieve all PPSK users  from ExtremeCloudIQ")
    page = 1

    ppskusers = []

    while page < 1000:
        url = URL + "/endusers?page=" + str(page) + "&limit=" + str(pageSize)
        print("Retrieving next page of PPSK users from ExtremeCloudIQ starting at page " +
              str(page) + " url: " + url)

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
        ppskusers = ppskusers + rawList

        if len(rawList) == 0:
            print("Reached the final page - stopping to retrieve users ")
            break

        page = page + 1

    return ppskusers

def get_random_string(length):
    letters = string.ascii_lowercase
    password = ''.join(random.choice(letters) for i in range(length))
    print("your password is:" + password)
    return password

login = GetaccessToken(username,password)
usergroups = listusergroups(10)

usergroupname = input("Enter the usergroup name: ")
usergroupId = 0
for usergroup in usergroups:
    if usergroup['name'] == usergroupname:
        usergroupId = usergroup['id']
        print("Found usergroup ID: " + str(usergroupId))
        break
if usergroupId == 0:
    print("Failed to retrieve data on User group by name: " + usergroupId)
    exit
print("\nIt's time to create the PPSK user\n")

name1 = input("Enter name: ")
user_name = input("Enter username: ")
email_address = input("Enter email-address: ")


adduser = CreatePPSKuser(usergroupId, name1, user_name)
if adduser == 0:
    print("\nFailed to create PPSK user - stopping\n")
    exit

users = retrievePPSKusers(10)
userId = 0
for user in users:
    if user['name'] == name1:
        userId = user['id']
        print("\nUser successfully created: \n" + str(name1))
        break

if userId == 0:
    print("\nThere is an issue creating the PPSK user - Failed to retrieve data on user by username\n" + name1)
    exit
