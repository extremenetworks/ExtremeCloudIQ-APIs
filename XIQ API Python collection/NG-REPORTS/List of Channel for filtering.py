import requests
         
baseUrl = 'https://api.extremecloudiq.com'
site_id = 'Site ID'
building_id = 'Building ID'
floor_id = 'Floor ID '
access_token = '***'

url = f"{baseUrl}/ng-reports/metadata/channel"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "site_ids": [
    site_id
  ],
  "building_ids": [
    building_id
  ],
  "floor_ids": [
    floor_id
  ],
  "ssids": [
    "string",
    "string"
  ],
  "bands": [
    "SIX_GHZ",
    "SIX_GHZ"
  ]
}


response = requests.post(url, headers=headers, params=params)

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
