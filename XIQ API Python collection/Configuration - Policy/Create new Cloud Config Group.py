import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/ccgs"

payload = json.dumps({
  "name": "NameOfCGG",
  "description": "Add New CCG",
  "device_ids": [
    0 # List of Device IDs to add to new CCG
  ]
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
