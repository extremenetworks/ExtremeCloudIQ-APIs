import requests
         
baseUrl = 'api.extremecloudiq.com'
device_id = 'device ID'
access_token = '***'

url = f"https://{baseUrl}/devices/country-code/:assign"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "devices": {
    "ids": [
      device_id
    ]
  },
  "country_code": "AFGHANISTAN_4"
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
