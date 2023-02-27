import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/devices/ibeacon"

payload = json.dumps({
  "device_ids": [
    0
  ],
  "enabled": True,
  "major": 65535,
  "minor": 65535,
  "power": 127,
  "enable_monitoring": True
})
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
