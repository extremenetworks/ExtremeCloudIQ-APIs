import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/deployments"

payload = json.dumps({
  "devices": {
    "ids": [
      0 # List of Device IDs to Push Configuration
    ]
  },
  "policy": {
    "enable_complete_configuration_update": True,
    "firmware_upgrade_policy": {
      "enable_enforce_upgrade": True,
      "enable_distributed_upgrade": True
    },
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
