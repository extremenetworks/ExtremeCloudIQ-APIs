import requests
         
baseUrl = 'api.extremecloudiq.com'
access_token = '***'

url = f"https://{baseUrl}/site/spectrum"
headers = {'Authorization': f'Bearer {access_token}'}
params = {'IsEmptyList': 'False'}
body = {
  "owner_id": 0,
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
