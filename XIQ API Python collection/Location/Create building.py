import requests
import json

access_token = '***'
parent_id = 0

url = "https://api.extremecloudiq.com/locations/building"

payload = json.dumps({
  "parent_id": str(parent_id),
  "name": "TheBuildingName",
  "address": "The building street address"
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
