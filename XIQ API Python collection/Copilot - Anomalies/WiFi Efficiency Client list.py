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
channel = 1
epoch_time = utc_seconds("2022-12-2 02:30:00", 'US/Eastern')
access_token = '***'

url = f"https://api.extremecloudiq.com/copilot/anomalies/wifi-efficiency/client-list?deviceId={device_id}&channel={channel}&timestamp={epoch_time}"

payload = {}
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
