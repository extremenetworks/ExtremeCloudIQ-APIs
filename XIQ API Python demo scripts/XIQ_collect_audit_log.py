#!/usr/bin/env python3
import json
from tracemalloc import start
import requests
import pandas as pd
import time
from datetime import datetime
from datetime import timedelta
from requests.exceptions import HTTPError
from pprint import pprint


# Global Objects
pagesize = '50' #Value can be added to set page size (1-100). If nothing in quotes default value will be used (10)
totalretries = 5

## TOKEN permission needs - "log:r"
XIQ_token = "***"
baseurl = "https://api.extremecloudiq.com"
HEADERS = {"Accept": "application/json", "Content-Type": "application/json", "Authorization": "Bearer " + XIQ_token}

# function that makes the API call with the provided url
# if pageCount is defined (all calls per hour after initial call) if the call fails they will be added to the secondtry list 
def get_api_call(url, page=0, pageCount=0,  startTime = '', endTime = '', msg='', count = 1):
    ## used for page if pagesize is set manually
    url_parms = []
    if page > 0:
        url_parms.append('page={}'.format(page))
    if pagesize:
        url_parms.append("limit={}".format(pagesize))
    if startTime:
        url_parms.append("startTime={}".format(startTime))
    if endTime:
        url_parms.append("endTime={}".format(endTime))
    if url_parms:
        if len(url_parms) > 1:
            parms_str = '&'.join(url_parms)
        else:
            parms_str = url_parms[0]
        #print(parms_str)
        url = "{}?{}".format(url, parms_str)
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
            error_msg = f"\n{response.json()}"
            raise TypeError(error_msg)   
        data = response.json()
        return data


def retrieveAuditLogs(startTime='',endTime=''):
    page = 0
    pageCount = 0
    firstCall = True
    log_data = []
    error_msg = 'to receive audit logs'
    url = "{}/logs/audit".format(baseurl)
    while page <= pageCount:
        for count in range(1, totalretries):
            try:
                data = get_api_call(url=url,page=page,pageCount=pageCount, startTime=startTime, endTime=endTime, msg=error_msg, count=count)
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
            totalCount = data['total_count']
            #countInPage = data['count']
            pageCount = data['total_pages']
            print(f"Collecting a total of {totalCount} logs...")
            firstCall = False
        page += 1
        log_data.extend(data['data'])
        
    return log_data

#def epochTimeConverter(time):
#    s = time / 1000.0
#    return datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S.%f')

def main():

    todayDate = time.strftime('%Y-%m-%d') 
    todayDateObj = datetime.strptime(todayDate, '%Y-%m-%d')
    todayEpoch = (todayDateObj.strftime('%s')) + '000'
    yesterday = todayDateObj - timedelta(days=1)
    yesterdayDate = yesterday.strftime('%Y-%m-%d')
    yesterdayEpoch = (yesterday.strftime('%s')) + '000'

    log_data = retrieveAuditLogs(startTime=yesterdayEpoch, endTime=todayEpoch)

    df = pd.DataFrame(log_data)
    #df['timestamp'] = df['timestamp'].apply(epochTimeConverter)
    df.to_csv("{}_Audit_log.csv".format(yesterdayDate),index=False)

if __name__ == '__main__':
	main()