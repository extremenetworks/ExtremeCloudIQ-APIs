import requests
         
ssid_id = 'SSID ID'
access_token = '***'

url = f"https://api.extremecloudiq.com/ssids/{ssid_id}/user-profile-assignment/:attach"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "user_profile_assignment_rules": [
    {
      "user_profile_id": 0,
      "user_profile_assignment_id": 0
    }
  ],
  "enable_user_profile_assignment": True,
  "enable_radius_attribute_user_profile_assignment": True,
  "attribute_type": "TUNNEL",
  "attribute_key": 0,
  "default_radius_client_object_id": 0
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
