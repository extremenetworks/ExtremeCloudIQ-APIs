import requests
import json

building_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/locations/building/{building_id}"

parent_id = 0
payload = json.dumps({
  "parent_id": str(parent_id),
  "name": "NewBuildingName",
  "address": "New building street address"
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
