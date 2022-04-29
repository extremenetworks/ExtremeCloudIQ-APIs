import requests
import json

device_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/devices/{device_id}/ssid/:override"

payload = json.dumps({
  "ssid_id": 0,
  "ssid": "string",
  "passphrase": "string"
})
headers = {
  'accept': '*/*',
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
