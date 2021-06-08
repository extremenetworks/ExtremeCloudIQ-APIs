import json
import getpass
import requests
import os
import logging

URL = "https://api.extremecloudiq.com"

print("XIQ CLI tool 2.0")
print("Enter your XIQ login credentials")
username = input("Email: ")
password = getpass.getpass("Password: ")

headers = {"Accept": "application/json", "Content-Type": "application/json"}

clicommand = input("Enter the CLI command: ")


#-------------------------
# logging
PATH = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(
    filename='{}/XIQ-CLI-output.log'.format(PATH),
    filemode='a',
    level=os.environ.get("LOGLEVEL", "INFO"),
    format= '%(asctime)s: %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'
)

# get access token
def GetaccessToken(username, password):
    url = URL + "/login"
    payload = json.dumps({"username": username, "password": password})
    response = requests.post(url, headers=headers, data=payload)
    if response is None:
        print("ERROR: Not able to login into ExtremeCloudIQ - no response!")
        return -1
    if response.status_code != 200:
        print(f"Error creating building in XIQ - HTTP Status Code: {str(response.status_code)}")
        raise TypeError(response)
    data = response.json()

    if "access_token" in data:
        print("Logged in and Got access token: " + data["access_token"])
        headers["Authorization"] = "Bearer " + data["access_token"]
        return 0

    else:
        raise TypeError("Unknown Error: Unable to gain access token")

# Get devices
def Getdevices(pageSize):

    print("Retrieving all devices from XIQ with page size of " + str(pageSize))
    page = 1
    devices = []

    while page < 1000:

        url =  URL + "/devices?page=" + \
              str(page) + "&limit=" + str(pageSize)

        print("Retrieving next page of devices from XIQ starting at page " +
              str(page) + " url: " + url)

        # Get the next page of devices
        response = requests.get(
            url, headers=headers, verify=True)
        if response is None:
            print("Error retrieving devices from XIQ - no response!")
            return

        if response.status_code != 200:
            print("Error retrieving devices from XIQ - HTTP Status Code: " +
                  str(response.status_code))
            print(response)
            return

        rawList = response.json()['data']
        print("Retrieved " + str(len(rawList)) + " devices on this page")
        print(rawList)
        devices = devices + rawList

        if len(rawList) == 0:
            print("Reached the final page - stopping to retrieve device data")
            break

        page = page + 1

    return devices

#send CLI
def sendCLI(deviceId, clicommand):
    url = URL + "/devices/:cli"
    payload = json.dumps({
        "devices": {
            "ids": [
                deviceId
            ]
        },
        "clis": [
            clicommand
        ]
    })

    response = requests.post(url, headers=headers, data=payload)

    if response is None:
        print("ERROR: Not able to login into ExtremeCloudIQ - no response!")
        return -1
    if response.status_code != 200:
        print(f"Error sending CLI command - HTTP Status Code: {str(response.status_code)}")
        raise TypeError(response)
    data = response.json()
    print(data)
    log_msg = data
    logging.error(log_msg)

try:
    login = GetaccessToken(username,password)
except TypeError as e:
    print(e)
    raise SystemExit
except:
    print("Unknown Error: Failed to generate token")
    raise SystemExit


devices = Getdevices(10)

deviceId = 0
for device in devices:
    try:
        deviceId = device['id']
        devicename = device['hostname']
        print("Device ids: " + str(deviceId) + " " + "hostname: " + str(devicename))
        log_msg = "Device ids: " + str(deviceId) + " " + "hostname: " + str(devicename)
        logging.error(log_msg)
        CLIsend= sendCLI(deviceId,clicommand)

    except:
        print("Unexpected error:")
