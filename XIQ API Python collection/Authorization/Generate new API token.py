import requests
import json
from datetime import datetime
import pytz

#Used to convert Time stamp to epochtime
def utc_seconds(str_dt, timezone):
    timezone = pytz.timezone(timezone)
    dt = datetime.strptime(str_dt, '%Y-%m-%d %H:%M:%S')
    dt_timezone = timezone.localize(dt)
    return int(dt_timezone.timestamp())

access_token = '***'

expire_time = utc_seconds("2022-7-2 02:30:00", 'US/Eastern')

url = "https://api.extremecloudiq.com/auth/apitoken"

payload = json.dumps({
  "description": "access_token for read account only",
  "expire_time": expire_time,
  "permissions": [
    "account:r"
  ]
})
headers = {
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
