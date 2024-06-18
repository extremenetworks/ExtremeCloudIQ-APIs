import requests
import json

device_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/devices/{device_id}/ftm-settings"

payload = json.dumps({
  "wgs84_override": True,
  "wgs84": {
    "latitude": 0,
    "longitude": 0,
    "altitude": 0
  },
  "zsubelement_override": True,
  "zsubelement": {
    "expected_to_move": True,
    "floor_number": 0,
    "above_floor": {
      "height": 0,
      "height_uncertainty": 0
    }
  },
  "civic_address_override": True,
  "civic_address": "string"
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
