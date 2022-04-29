import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/user-profiles"

payload = json.dumps({
  "name": "Testing",
  "vlan_profile_id": 0
})

headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
