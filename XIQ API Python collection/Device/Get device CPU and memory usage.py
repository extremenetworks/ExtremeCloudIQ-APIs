import requests
from datetime import datetime
import pytz

#Used to convert Time stamp to epochtime
def utc_seconds(str_dt, timezone):
    timezone = pytz.timezone(timezone)
    dt = datetime.strptime(str_dt, '%Y-%m-%d %H:%M:%S')
    dt_timezone = timezone.localize(dt)
    return int(dt_timezone.timestamp()*1000) # epoch time in milliseconds

device_id = 0
myStartTime = utc_seconds("2022-12-2 02:30:00", 'US/Eastern')
myEndTime = utc_seconds("2023-2-23 02:30:00", 'US/Eastern')
access_token = '***'

url = f"https://api.extremecloudiq.com/devices/{device_id}/history/cpu-mem?startTime={myStartTime}&endTime={myEndTime}&interval=1"

payload={}
headers = {
  'accept': '*/*',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
