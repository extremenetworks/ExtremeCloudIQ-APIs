import requests
import json


url = "https://api.extremecloudiq.com/devices/client-monitor/:assign"

payload = json.dumps({
  "devices": {
    "ids": [
      0
    ]
  },
  "client_monitor": {
    "client_monitor_profile_id": 0,
    "enable": True
  }
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
