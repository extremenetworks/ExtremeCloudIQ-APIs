#!/usr/bin/env python3
from typing import Collection
import requests
import json
from requests.exceptions import HTTPError



# Global Objects
# location to send commands
location_id = "769490635818704"
# A list of Models to receive the cli commands. If none listed all devices with receive the cli commands at the location
model_filter = ["AP_410C"]
cli_commands = ["show idm","show capwap client"]
pagesize = '' #Value can be added to set page size. If nothing in quotes default value will be used (10). Page Size, min = 1, max = 100
totalretries = 5


# generated xiq token with minimum "device:list, device, device:cli" permissions
XIQ_token = "****"
baseurl = "https://api.extremecloudiq.com"
HEADERS = {"Accept": "application/json", "Content-Type": "application/json", "Authorization": "Bearer " + XIQ_token}


# function that makes the API call with the provided url
# if pageCount is defined (all calls per hour after initial call) if the call fails they will be added to the secondtry list 
def get_api_call(url, page=0, pageCount=0,  msg='', count = 1):
    ## used for page if pagesize is set manually
    url_parms = []
    if page > 0:
        url = url + '&page={}'.format(page)
    if pagesize:
        url = url + "&limit={}".format(pagesize)
    #print(url)
    
    ## the first call will not show as the data returned is used to collect the total count of Clients which is used for the page count
    #print(f"####  {url}  ####")
    if pageCount != 0:
        print("API call {} page {:>2} of {:2} - attempt {} of {}".format(msg,page, pageCount, count, totalretries), end=": ")
    else:
        print("Attempting call {} - attempt {} of {}".format(msg, count, totalretries), end=": ")
    try:
        response = requests.get(url, headers=HEADERS, timeout=60)
    except HTTPError as http_err:
        raise HTTPError(f'HTTP error occurred: {http_err} - on API {url}')  
    except Exception as err:
        raise TypeError(f'Other error occurred: {err}: on API {url}')
    else:
        if response is None:
            error_msg = f"Error retrieving API {msg} from XIQ - no response!"
            raise TypeError(error_msg)
        elif response.status_code != 200:
            error_msg = f"Error retrieving API {msg} from XIQ - HTTP Status Code: {str(response.status_code)}"
            raise TypeError(error_msg)   
        data = response.json()
        return data

def post_api_call(url, payload = {}, msg='', count = 1):
    #print(f"####  {url}  ####")

    print("Attempting call {} - attempt {} of {}".format(msg, count, totalretries), end=": ")
    try:
        response = requests.post(url, headers=HEADERS, data=payload, timeout=60)
    except HTTPError as http_err:
        raise HTTPError(f'HTTP error occurred: {http_err} - on API {url}')  
    except Exception as err:
        raise TypeError(f'Other error occurred: {err}: on API {url}')
    else:
        if response is None:
            error_msg = f"Error retrieving API {msg} from XIQ - no response!"
            raise TypeError(error_msg)
        elif response.status_code != 200:
            error_msg = f"Error retrieving API {msg} from XIQ - HTTP Status Code: {str(response.status_code)}"
            raise TypeError(error_msg)   
        data = response.json()
        return data
    

# Retrieves IDs for all devices
def retrieveDeviceIDs(location_id):
    global isModelFilter
    page = 0
    pageCount = 0
    firstCall = True
    device_data = {}
    error_msg = 'to receive device list'
    url = "{}/devices?locationId={}".format(baseurl,location_id)
    while page <= pageCount:    
        for count in range(1, totalretries):
            try:
                data = get_api_call(url,page,pageCount, error_msg, count)
            except TypeError as e:
                print(f"API failed with {e}")
                count+=1
                success = False
            except HTTPError as e:
                print(f"API HTTP Error {e}")
                count+=1
                success = False
            except:
                print(f"API failed {error_msg} with an unknown API error:\n 	{url}")		
                count+=1
                success = False
            else:
                print("Successful Connection")
                success = True
                break
        if success == False:
            print(f"API call {error_msg} failed too many times. Script is exiting...")
            raise SystemExit
        if firstCall == True:
            page = data['page']
            #totalCount = data['total_count']
            #countInPage = data['count']
            pageCount = data['total_pages']
            firstCall = False
        page += 1
        for device in data['data']:
            if isModelFilter:
                if device['product_type'] in model_filter:
                    device_data[device['id']] = device['hostname']
            else:
                device_data[device['id']] = device['hostname']
    return(device_data)

def sendCLI(site_device_ids, cli_commands):
    error_msg = "to send CLI command"
    payload = json.dumps({
                        "devices": {
                            "ids": site_device_ids
                        },
                        "clis": cli_commands
                        })
    #print(payload)                    
    url = "{}/devices/:cli".format(baseurl)
    for count in range(1, totalretries):
        try:
            data = post_api_call(url, payload, error_msg, count=count)
        except TypeError as e:
            print(f"API failed with {e}")
            count+=1
            success = False
        except HTTPError as e:
            print(f"API HTTP Error {e}")
            count+=1
            success = False
        except:
            print(f"API failed {error_msg} with an unknown API error:\n 	{url}")		
            count+=1
            success = False
        else:
            print("Successful Connection")
            success = True
            break
    if success == False:
        print(f"API call {error_msg} failed too many times. Script is exiting...")
        raise SystemExit
    return(data)

isModelFilter = False

def main():
    global isModelFilter
    if model_filter:
        isModelFilter = True
    #number of devices to gather location info simultaneously
    sizeofdevicebatch = 500
    data = {}
    ap_data = retrieveDeviceIDs(location_id)
    ap_ids = list(ap_data.keys())

    for i in range(0, len(ap_ids), sizeofdevicebatch):
        batch = ap_ids[i:i+sizeofdevicebatch]
        response = sendCLI(batch, cli_commands)
        data.update(response['device_cli_outputs'])
    print('\n\n')
    print()
    print("{:^30} {:^30} {:^30}".format("DEVICE NAME", "CLI COMMAND", "CLI RESPONSE"))
    for i in range(1, 100 ,1):
        print('-', end='')
    print()
    for apname, responses in data.items():
        for response in responses:
            print("************************\n************************\n{:^30} {:<30} \n\n************************\n{}".format(ap_data[int(apname)], response['cli'], response['output']))

if __name__ == '__main__':
	main()