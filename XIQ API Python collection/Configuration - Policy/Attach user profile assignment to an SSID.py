import requests
import json

ssid_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/ssids/{ssid_id}/user-profile-assignment/:attach"

payload = json.dumps({
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
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
