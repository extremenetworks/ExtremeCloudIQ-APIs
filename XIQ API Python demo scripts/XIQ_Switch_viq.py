#!/usr/bin/env python3
import requests
import getpass
import json
from pprint import pprint
from requests.exceptions import HTTPError

URL = "https://api.extremecloudiq.com"
headers = {"Accept": "application/json", "Content-Type": "application/json"}

currentViqName =  ''
currentViqID = ''

def get_api_call(url):
        try:
            response = requests.get(url, headers= headers)
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err} - on API {url}')
            raise ValueError(f'HTTP error occurred: {http_err}') 
        if response is None:
            log_msg = "ERROR: No response received from XIQ!"
            print(log_msg)
            raise ValueError(log_msg)
        if response.status_code != 200:
            log_msg = f"Error - HTTP Status Code: {str(response.status_code)}"
            print(f"{log_msg}")
            print(f"\t\t{response}")
            raise ValueError(log_msg)  
        try:
            data = response.json()
        except json.JSONDecodeError:
            print(f"Unable to parse json data - {url} - HTTP Status Code: {str(response.status_code)}")
            raise ValueError("Unable to parse the data from json, script cannot proceed")
        return data

def post_api_call(url, payload):
        try:
            response = requests.post(url, headers= headers, data=payload)
        except HTTPError as http_err:
            raise ValueError(f'HTTP error occurred: {http_err}') 
        if response is None:
            log_msg = "ERROR: No response received from XIQ!"
            raise ValueError(log_msg)
        if response.status_code == 202:
            return "Success"
        elif response.status_code != 200:
            log_msg = f"Error - HTTP Status Code: {str(response.status_code)}"
            print(f"{log_msg}")
            try:
                data = response.json()
            except json.JSONDecodeError:
                print(f"\t\t{response.text()}")
            else:
                if 'error_message' in data:
                    print(f"\t\t{data['error_message']}")
                    raise Exception(data['error_message'])
            raise ValueError(log_msg)
        try:
            data = response.json()
        except json.JSONDecodeError:
            print(f"Unable to parse json data - {url} - HTTP Status Code: {str(response.status_code)}")
            raise ValueError("Unable to parse the data from json, script cannot proceed")
        return data


def getAccessToken(user_name, password):
        info = "get XIQ token"
        success = 0
        url = URL + "/login"
        payload = json.dumps({"username": user_name, "password": password})
        try:
            data = post_api_call(url=url,payload=payload)
        except ValueError as e:
            print(f"API to {info} failed with {e}")
        except Exception as e:
            print(f"API to {info} failed with {e}")
            print('script is exiting...')
            raise SystemExit
        except:
            print(f"API to {info} failed with unknown API error")
        else:
            success = 1
        if success != 1:
            print("failed to get XIQ token. Cannot continue to import")
            print("exiting script...")
            raise SystemExit
        
        if "access_token" in data:
            #print("Logged in and Got access token: " + data["access_token"])
            headers["Authorization"] = "Bearer " + data["access_token"]
            return 0

        else:
            log_msg = "Unknown Error: Unable to gain access token for XIQ"
            raise ValueError(log_msg)

# EXTERNAL ACCOUNTS
def getVIQInfo():
    global currentViqName
    global currentViqID

    info="get current VIQ name"
    success = 0
    url = "{}/account/home".format(URL)
    try:
        data = get_api_call(url=url)
    except ValueError as e:
        print(f"API to {info} failed with {e}")
    except:
        print(f"API to {info} failed with unknown API error")
    else:
        success = 1
    if success != 1:
        print(f"Failed to {info}")
        return 1   
    else:
        currentViqName = data['name']
        currentViqID = data['id']

#ACCOUNT SWITCH
def selectManagedAccount():
    global currentViqName
    getVIQInfo()
    info="gather accessible external XIQ acccounts"
    success = 0
    url = "{}/account/external".format(URL)
    try:
        data = get_api_call(url=url)
    except ValueError as e:
        print(f"API to {info} failed with {e}")
    except:
        print(f"API to {info} failed with unknown API error")
    else:
        success = 1
    if success != 1:
        print(f"Failed to {info}")
        return 1
        
    else:
        return(data, currentViqName)

def switchAccount(viqID, viqName):
    info=f"switch to external account {viqName}"
    success = 0
    url = "{}/account/:switch?id={}".format(URL,viqID)
    payload = ''
    try:
        data = post_api_call(url=url, payload=payload)
    except ValueError as e:
        print(f"API to {info} failed with {e}")
    except Exception as e:
        print(f"API to {info} failed with {e}")
        print('script is exiting...')
        raise SystemExit
    except:
        print(f"API to {info} failed with unknown API error")
    else:
        success = 1
    if success != 1:
        print("failed to get XIQ token to {}. Cannot continue to import".format(info))
        print("exiting script...")
        raise SystemExit
    
    if "access_token" in data:
        #print("Logged in and Got access token: " + data["access_token"])
        headers["Authorization"] = "Bearer " + data["access_token"]
        getVIQInfo()
        if viqName != currentViqName:
            print("Failed to switch to external account!!")
            print("Script is exiting...")
            raise SystemExit
        return 0
    else:
        log_msg = "Unknown Error: Unable to gain access token for XIQ"
        raise ValueError(log_msg) 

#MAIN

print("Enter your XIQ login credentials")
user_name = input("Email: ")
password = getpass.getpass("Password: ")


try:
    getAccessToken(user_name, password)
except ValueError as e:
        print(e)
        raise SystemExit
except HTTPError as e:
   print(e)
   raise SystemExit

accounts, currentViqName = selectManagedAccount()
if accounts == 1:
    print("No External accounts found.")
    raise SystemExit
elif accounts:
    for account in accounts: 
        newViqId = account['id']
        newViqName = account['name']
        switchAccount(newViqId, newViqName)
        print(currentViqName, currentViqID)

