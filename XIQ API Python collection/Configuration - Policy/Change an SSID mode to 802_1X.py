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
  "radius_server_group_id": 0,
  "user_group_ids": [
    0
  ]
})
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
