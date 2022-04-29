import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/devices/os/:change"

device_id = 0
payload = json.dumps({
  "device_ids": [
    0
  ],
  "target_os": "WiNG"
})
headers = {
  'accept': '*/*',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
