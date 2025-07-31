import requests
         
baseUrl = 'https://api.extremecloudiq.com'
access_token = '***'

url = f"{baseUrl}/devices/ibeacon"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "device_ids": [
    0
  ],
  "enabled": True,
  "major": 65535,
  "minor": 65535,
  "power": 127,
  "enable_monitoring": True
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
