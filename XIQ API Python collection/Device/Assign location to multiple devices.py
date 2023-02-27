import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/devices/location/:assign"

payload = json.dumps({
  "devices": {
    "ids": [
      0
    ],
    "device_locations":{
      "location_id": 0,
      "x": 0,
      "y": 0,
      "latitude": 0,
      "longitude": 0
    }
  }
})
headers = {
  'accept': '*/*',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
