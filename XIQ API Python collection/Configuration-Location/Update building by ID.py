import requests
import json

url = "https://api.extremecloudiq.com/locations/building/{{building_id}}"

payload = json.dumps({
  "parent_id": "123456",
  "name": "NewBuildingName",
  "address": "New building street address"
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
