import requests
import json

device_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/devices/{device_id}/ssid/status/:change"


payload = json.dumps({
  "ssid_ids": [
    0
  ],
  "if_names": [
    "WIFI0"
  ],
  "enabled": True
})
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
