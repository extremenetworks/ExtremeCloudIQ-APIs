import requests
         
baseUrl = 'api.extremecloudiq.com'
device_id = 'device ID'
access_token = '***'

url = f"https://{baseUrl}/devices/{device_id}/ftm-settings"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
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
}


response = requests.put(url, headers=headers, params=params)

print("Status Code:", response.status_code)

content_type = response.headers.get('Content-Type')
if content_type and 'application/json' in content_type:
    try:
        print("Response Body:", response.json())
    except ValueError:
        print("Response is not valid JSON")
else:
    print("Content-Type is not application/json")
    print(response.text)
