import requests
from datetime import datetime
import pytz

#Used to convert Time stamp to epochtime
def utc_seconds(str_dt, timezone):
    timezone = pytz.timezone(timezone)
    dt = datetime.strptime(str_dt, '%Y-%m-%d %H:%M:%S')
    dt_timezone = timezone.localize(dt) 
    return int(dt_timezone.timestamp()*1000) # epoch time in milliseconds)                 

         
baseUrl = 'api.extremecloudiq.com'
device_id = 'device ID'
myStartTime = utc_seconds('2024-12-07 02:30:00', 'US/Eastern')
myEndTime = utc_seconds('2024-12-07 02:30:00', 'US/Eastern')
access_token = '***'

url = f"https://{baseUrl}/d360/client/grid"
headers = {'Authorization': f'Bearer {access_token}'}
params = {'page': '1', 'limit': '10', 'deviceId': f'{device_id}', 'startTime': f'{myStartTime}', 'endTime': f'{myEndTime}'}
body = {
  "number_filter": [
    {
      "column_name": "string",
      "filter_type": "GT",
      "value": 0,
      "min": 0,
      "max": 0
    }
  ],
  "alias": [
    "string"
  ],
  "auth_methods": [
    "string"
  ],
  "encryption_methods": [
    "string"
  ],
  "operating_systems": [
    "string"
  ],
  "ssids": [
    "string"
  ],
  "user_profiles": [
    "string"
  ],
  "frequency": [
    "string"
  ],
  "category_assignments": [
    "string"
  ]
}
# keyword: None (disabled)
# clientStatus: TOTAL (disabled)
# sortField: None (disabled)
# sortOrder: ASC (disabled)
# connectionStatus: CONNECTED (disabled)

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
