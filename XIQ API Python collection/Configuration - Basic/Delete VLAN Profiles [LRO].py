import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/vlan-profiles/:delete?async=false"

payload = json.dumps({
  "ids": [
    0 # List of Device IDs to delete VLAN Profiles
  ]
})
headers = {
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.headers) # LRO location URL is included in headers
print(response.text)
