import requests
import json

site_id = 0
parent_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/locations/site/{site_id}"

payload = json.dumps({
  "parent_id": str(parent_id),
  "name": "NewSiteName",
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

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
