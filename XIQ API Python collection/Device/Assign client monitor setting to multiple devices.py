import requests
         
baseUrl = 'api.extremecloudiq.com'
access_token = '***'

url = f"https://{baseUrl}/devices/client-monitor/:assign"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "devices": {
    "ids": [
      0
    ]
  },
  "client_monitor": {
    "client_monitor_profile_id": 0,
    "enable": True
  }
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
