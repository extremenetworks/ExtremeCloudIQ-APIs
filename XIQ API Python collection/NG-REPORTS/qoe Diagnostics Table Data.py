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

url = f"{baseUrl}/ng-reports/tabledata"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "building_ids": [
    building_id
  ],
  "end_time": myEndTime,
  "floor_ids": [
    floor_id
  ],
  "metrics": "CLIENT_AIRTIME_USAGE",
  "site_ids": [
    site_id
  ],
  "sort_field": "TIME_STAMP",
  "sort_order": "ASC",
  "start_time": myStartTime,
  "bands": [
    "FIVE_GHZ",
    "TWO_GHZ"
  ],
  "contypes": [
    "UNKNOWN",
    "THREAD"
  ],
  "devicetypes": [
    "WIRELESS",
    "WIRELESS"
  ],
  "vlan_ids": [
    2355,
    1486
  ],
  "device_ids": [
    6168,
    8287
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
    8002,
    5813
  ],
  "app_ids": [
    118,
    6920
  ],
  "channel_nums": [
    3815,
    1773
  ],
  "admin_roles": [
    3162,
    4131
  ],
  "page_no": 1,
  "limit": 1,
  "export_data": False,
  "search_parameter": "string",
  "async": False,
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
