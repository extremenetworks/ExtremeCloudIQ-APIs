import requests
import json
from datetime import datetime
import pytz

#Used to convert Time stamp to epochtime
def utc_seconds(str_dt, timezone):
    timezone = pytz.timezone(timezone)
    dt = datetime.strptime(str_dt, '%Y-%m-%d %H:%M:%S')
    dt_timezone = timezone.localize(dt)
    return int(dt_timezone.timestamp()*1000) # epoch time in milliseconds

epoch_time = utc_seconds("2022-12-2 02:30:00", 'US/Eastern')
access_token = '***'

url = "https://api.extremecloudiq.com/deployments"

payload = json.dumps({
  "schedule": {
    "start_time": epoch_time
  },
  "devices": {
    "ids": [
      0   # List of Device IDs to Push Configuration
    ],
    "site_ids": [
      0   # List of Site IDs to Push Configuration
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
})

headers = {
  'accept': '*/*',
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
