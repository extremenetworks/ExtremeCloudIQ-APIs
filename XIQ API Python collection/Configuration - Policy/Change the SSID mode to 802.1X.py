import requests
         
ssid_id = 'SSID ID'
access_token = '***'

url = f"https://api.extremecloudiq.com/ssids/{ssid_id}/mode/dot1x"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "key_management": "WPA3_8021X",
  "encryption_method": "CCMP",
  "enable_idm": True,
  "transition_mode": True,
  "radius_server_group_id": 0,
  "user_group_ids": [
    0
  ]
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
