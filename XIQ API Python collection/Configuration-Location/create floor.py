import requests
import json

url = "https://api.extremecloudiq.com/locations/floor"

payload = json.dumps({
  "parent_id": "654321",
  "name": "TheFloorName",
  "environment": "RF_ENVIRONMENT_TYPE_AUTO_ESTIMATE",
  "db_attenuation": "15",
  "measurement_unit": "MEASUREMENT_UNIT_FEET",
  "installation_height": "12",
  "map_size_width": "12",
  "map_size_height": "12",
  "map_name": ""
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
