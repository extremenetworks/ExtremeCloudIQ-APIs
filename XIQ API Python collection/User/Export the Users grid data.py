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
myStartTime = utc_seconds('2024-12-07 02:30:00', 'US/Eastern')
myEndTime = utc_seconds('2024-12-07 02:30:00', 'US/Eastern')
site_id = 'Site ID'
access_token = '***'

url = f"{baseUrl}/users/grid_export"
headers = {'Authorization': f'Bearer {access_token}'}
params = {'startTime': f'{myStartTime}', 'endTime': f'{myEndTime}'}
body = {
  "user_name": [
    "string",
    "string"
  ],
  "source": [
    "string",
    "string"
  ],
  "site_ids": [
    site_id
  ],
  "status": True,
  "duration": [
    {
      "column_name": "string",
      "filter_type": "NEQ",
      "value": 2907,
      "min": 1313,
      "max": 7816
    },
    {
      "column_name": "string",
      "filter_type": "NEQ",
      "value": 5746,
      "min": 1160,
      "max": 3054
    }
  ],
  "user_ids": [
    2214,
    7804
  ]
}
# search: string (disabled)
# sortField: SESSION_DURATION (disabled)
# order: ASC (disabled)

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
