import requests
import json

np_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/network-policies/{np_id}/ssids/:remove"

ssid_id = 0
payload = f"[\n  {ssid_id}\n]"
headers = {
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
