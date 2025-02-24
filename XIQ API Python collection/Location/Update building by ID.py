import requests
         
building_id = 'Building ID'
loc_id = 'Location ID'
access_token = '***'

url = f"https://api.extremecloudiq.com/locations/building/{building_id}"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "parent_id": "loc_id",
  "name": "NewBuildingName",
  "address": {
    "address": "string",
    "address2": "string",
    "city": "string",
    "state": "string",
    "postal_code": "string"
  }
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
