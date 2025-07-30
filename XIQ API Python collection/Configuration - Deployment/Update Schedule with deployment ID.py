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
deployment_id = 'Deployment ID'
myEpoch = utc_seconds('2024-12-07 02:30:00', 'US/Eastern')
device_id = 'device ID'
site_id = 'Site ID'
access_token = '***'

url = f"{baseUrl}/deployments/{deployment_id}"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "schedule": {
    "start_time": myEpoch
  },
  "devices": {
    "ids": [
      device_id
    ],
    "site_ids": [
      site_id
    ]
  },
  "policy": {
    "enable_complete_configuration_update": True,
    "firmware_upgrade_policy": {
      "enable_enforce_upgrade": True,
      "enable_distributed_upgrade": True
    },
    "firmware_upgrade_versions": [
      {
        "firmware_id": 0,
        "device_id": 0,
        "product_type": "string"
      }
    ],
    "firmware_activate_option": {
      "enable_activate_at_next_reboot": True,
      "activation_delay_seconds": 0,
      "activation_time": 0
    }
  }
}


response = requests.put(url, headers=headers, params=params)

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
