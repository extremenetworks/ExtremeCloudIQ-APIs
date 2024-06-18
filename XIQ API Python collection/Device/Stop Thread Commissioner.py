import requests
import json

device_id = 0 
access_token = '***'

url = f"https://api.extremecloudiq.com/devices/{device_id}/thread/commissioner/:stop"

payload = json.dumps({
  "device_id": 0,
  "interface_name": "string"
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
