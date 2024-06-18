import requests
import json

ssid_id = 0
radius_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/ssids/{ssid_id}/radius-client-profile/:attach"

payload = json.dumps(radius_id)
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
