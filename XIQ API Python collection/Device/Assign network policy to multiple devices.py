import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/devices/network-policy/:assign"

payload = json.dumps({
  "devices": {
    "ids": [
      0
    ]
  },
  "network_policy_id": 0
})
headers = {
  'accept': '*/*',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
