import requests
import json

user_profile_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/user-profiles/{user_profile_id}"

payload = json.dumps({
  "name": "string",
  "vlan_profile_id": 0
})
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
