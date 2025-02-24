import requests
         
ssid_id = 'SSID ID'
access_token = '***'

url = f"https://api.extremecloudiq.com/ssids/{ssid_id}/mode/wep"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "key_management": "WEP_8021X",
  "encryption_method": "WEP104",
  "authentication_method": "OPEN",
  "default_key": "FIRST",
  "key_type": "ASCII",
  "key_value": "abcd123456789",
  "key_value2": "string",
  "key_value3": "string",
  "key_value4": "string",
  "radius_server_group_id": 0
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
