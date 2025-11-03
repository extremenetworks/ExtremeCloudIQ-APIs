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
device_id = 'device ID'
app_id = 'Application ID'
access_token = '***'

url = f"{baseUrl}/ng-reports/downloads/reports"
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
  "site_ids": [
    site_id
  ],
  "start_time": myStartTime,
  "metrics": [
    "TRAFFIC_VOLUME_PER_APP",
    "DEVICES_BY_CLIENTS"
  ],
  "bands": [
    "FIVE_GHZ",
    "SIX_GHZ"
  ],
  "contypes": [
    "THREAD",
    "THREAD"
  ],
  "devicetypes": [
    "WIRELESS",
    "WIRELESS"
  ],
  "vlan_ids": [
    1183,
    1493
  ],
  "device_ids": [
    device_id
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
    5842,
    3046
  ],
  "app_ids": [
    app_id
  ],
  "channel_nums": [
    5828,
    9800
  ],
  "admin_roles": [
    9234,
    9758
  ],
  "export_data": False,
  "search_parameter": "string",
  "async": False,
  "mode": "SNAPSHOT",
  "download_type": "CSV",
  "limit": 2105,
  "page": 7893,
  "time_offset": 207,
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
