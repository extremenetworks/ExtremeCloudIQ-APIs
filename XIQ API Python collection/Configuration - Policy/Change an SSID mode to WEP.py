import requests
import json

ssid_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/ssids/{ssid_id}/mode/wep"

payload = json.dumps({
  "key_management": "WEP_8021X",
  "encryption_method": "WEP104",
  "authentication_method": "OPEN",
  "default_key": "FIRST",
  "key_type": "ASCII",
  "key_value": "abcd123456789",
  "key_value2": "string",
  "key_value3": "string",
  "key_value4": "string",
  "radius_server_group_id": 0
})
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
