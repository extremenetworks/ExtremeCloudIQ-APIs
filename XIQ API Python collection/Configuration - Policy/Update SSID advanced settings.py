import requests
import json

ssid_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/ssids/advanced-settings/{ssid_id}"

payload = json.dumps({
  "enable802_dot11mc": True
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
