import requests
import json

np_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/pcgs/key-based/network-policy-{np_id}/:onboard"

payload = json.dumps({
  "ssid_name": "string",
  "enabled": True,
  "user_ids": [
    0
  ]
})
headers = {
  'accept': '*/*',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
