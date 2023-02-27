import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/devices/location/:query"

payload = json.dumps({
  "ids": [
    0 # List of Device IDs to collect locations
  ]
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
