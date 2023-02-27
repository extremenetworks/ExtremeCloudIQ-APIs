import requests
import json

ssid_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/ssids/{ssid_id}/mode/dot1x"

payload = json.dumps({
  "key_management": "WPA3_8021X",
  "encryption_method": "CCMP",
  "enable_idm": True,
  "transition_mode": True,
  "radius_server_group_id": 0, # The RADIUS server group ID if not using ExtremeCloud IQ Authentication Service
  "user_group_ids": [
    0 # The user group IDs if using ExtremeCloud IQ Authentication Service
  ]
})
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
