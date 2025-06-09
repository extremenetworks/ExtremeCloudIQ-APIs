import requests
         
baseUrl = 'api.extremecloudiq.com'
floor_id = 'Floor ID '
building_id = 'Building ID'
access_token = '***'

url = f"https://{baseUrl}/locations/floor/{floor_id}"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "parent_id": "building_id",
  "name": "string",
  "environment": "AUTO_ESTIMATE",
  "db_attenuation": "15",
  "measurement_unit": "FEET",
  "installation_height": "12",
  "map_size_width": "12",
  "map_size_height": "12",
  "map_name": "string"
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
