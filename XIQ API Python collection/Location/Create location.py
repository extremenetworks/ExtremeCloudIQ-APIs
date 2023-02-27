import requests
import json


parent_id = 0
access_token = '***'

url = "https://api.extremecloudiq.com/locations/"


payload = json.dumps({
  "parent_id": str(parent_id),
  "name": "Location Name",
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
