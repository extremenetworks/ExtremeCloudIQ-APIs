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
access_token = '***'

url = f"{baseUrl}/copilot/anomalies/devices-with-locations"
headers = {'Authorization': f'Bearer {access_token}'}
params = {'page': '1', 'limit': '10', 'startTime': f'{myStartTime}', 'endTime': f'{myEndTime}'}

# anomalyType: None (disabled)
# buildingId: {{building_id}} (disabled)
# severity: None (disabled)
# excludeMuted: false (disabled)
# sortField: None (disabled)
# sortOrder: ASC (disabled)
# searchKey: None (disabled)

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
