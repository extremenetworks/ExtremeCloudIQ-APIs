import requests
import json

parent_id = 0
access_token = '***'

url = "https://api.extremecloudiq.com/locations/site"

payload = json.dumps({
  "parent_id": parent_id,
  "name": "Site Name",
  "address": {
    "address": "string",
    "address2": "string",
    "city": "string",
    "state": "string",
    "postal_code": "string"
  },
  "country_code": 0
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
