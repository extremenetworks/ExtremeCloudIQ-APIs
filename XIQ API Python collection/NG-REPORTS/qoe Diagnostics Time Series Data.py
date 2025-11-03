import requests
from datetime import datetime
import pytz

#Used to convert Time stamp to epochtime
def utc_seconds(str_dt, timezone):
    timezone = pytz.timezone(timezone)
    dt = datetime.strptime(str_dt, '%Y-%m-%d %H:%M:%S')
    dt_timezone = timezone.localize(dt) 
    return int(dt_timezone.timestamp()*1000) # epoch time in milliseconds)                 

         
baseUrl = 'https://api.extremecloudiq.com'
building_id = 'Building ID'
myEndTime = utc_seconds('2024-12-07 02:30:00', 'US/Eastern')
floor_id = 'Floor ID '
site_id = 'Site ID'
myStartTime = utc_seconds('2024-12-07 02:30:00', 'US/Eastern')
access_token = '***'

url = f"{baseUrl}/ng-reports/timeseries"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "async": False,
  "building_ids": [
    building_id
  ],
  "end_time": myEndTime,
  "floor_ids": [
    floor_id
  ],
  "metrics": "WIRELESS_CLIENTS_BY_OS",
  "site_ids": [
    site_id
  ],
  "start_time": myStartTime,
  "bands": [
    "FIVE_GHZ",
    "TWO_GHZ"
  ],
  "contypes": [
    "WIRELESS",
    "WIRELESS"
  ],
  "devicetypes": [
    "WIRED",
    "WIRELESS"
  ],
  "vlan_ids": [
    6758,
    313
  ],
  "device_ids": [
    5598,
    9945
  ],
  "ssids": [
    "string",
    "string"
  ],
  "user_names": [
    "string",
    "string"
  ],
  "client_macs": [
    "string",
    "string"
  ],
  "port_nums": [
    4402,
    536
  ],
  "app_ids": [
    4354,
    8243
  ],
  "channel_nums": [
    2934,
    8705
  ],
  "admin_roles": [
    8970,
    5618
  ],
  "page": 4530,
  "limit": 6219,
  "os_types": [
    "string",
    "string"
  ],
  "isSSIDSelected": True,
  "isBandSelected": True
}


response = requests.post(url, headers=headers, params=params)

print("Status Code:", response.status_code)

content_type = response.headers.get('Content-Type')
if content_type and 'application/json' in content_type:
    try:
        print("Response Body:", response.json())
    except ValueError:
        print("Response is not valid JSON")
else:
    print("Content-Type is not application/json")
    print(response.text)
