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
myStartTime = utc_seconds('2024-12-07 02:30:00', 'US/Eastern')
myEndTime = utc_seconds('2024-12-07 02:30:00', 'US/Eastern')
access_token = '***'

url = f"https://{baseUrl}/copilot/anomalies/report"
headers = {'Authorization': f'Bearer {access_token}'}
params = {'endTime': f'{myEndTime}', 'startTime': f'{myStartTime}', 'offsetTime': '0'}

# anomalyId: {{anomaly_id}} (disabled)
# buildingId: {{building_id}} (disabled)
# severity:  (disabled)
# excludeMuted: false (disabled)
# sortField:  (disabled)
# sortOrder: ASC (disabled)
# searchKey:  (disabled)
# fileType: csv (disabled)

response = requests.get(url, headers=headers, params=params)

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
