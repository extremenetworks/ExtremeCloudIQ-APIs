import requests
import json

owner_id = 0
access_token = '***'

url = "https://api.extremecloudiq.com/ap/spectrum"

payload = json.dumps({
  "owner_id": owner_id,
  "site_name": "string",
  "region": "US",
  "input_info": [
    {
      "serial_number": "string",
      "coordinates": {
        "latitude": 0,
        "longitude": 0,
        "timestamp": 0
      },
      "elevation": {
        "height": 0,
        "height_reference": "AGL",
        "uncertainty": 0
      },
      "ellipse": {
        "major_axis": 0,
        "minor_axis": 0,
        "orientation": 0
      },
      "environment": "INDOOR"
    }
  ]
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
