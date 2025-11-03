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
site_id = 'Site ID'
building_id = 'Building ID'
floor_id = 'Floor ID '
myStartTime = utc_seconds('2024-12-07 02:30:00', 'US/Eastern')
myEndTime = utc_seconds('2024-12-07 02:30:00', 'US/Eastern')
access_token = '***'

url = f"{baseUrl}/ng-reports/metadata/ssids"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "site_ids": [
    site_id
  ],
  "building_ids": [
    building_id
  ],
  "floor_ids": [
    floor_id
  ],
  "start_time": myStartTime,
  "end_time": myEndTime
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
