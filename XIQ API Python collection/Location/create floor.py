import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/locations/floor"

building_id = 0
payload = json.dumps({
  "parent_id": str(building_id),
  "name": "TheFloorName",
  "environment": "AUTO_ESTIMATE",
  "db_attenuation": "15",
  "measurement_unit": "FEET",
  "installation_height": "12",
  "map_size_width": "12",
  "map_size_height": "12",
  "map_name": ""
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
