import requests
import json

np_id = 0 
access_token = '***'

url = f"https://api.extremecloudiq.com/network-policies/{np_id}/ssids/:add"

payload = json.dumps([
  0 #ssid_id
  ])
headers = {
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
