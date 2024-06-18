import requests
import json

user_profile_id = 0
mac_firewall_policy_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/user-profiles/{user_profile_id}/mac-filrewall-policies/:attach"

payload = json.loads({
    "policy_id": mac_firewall_policy_id,
    "traffic": "INBOUND"
    })
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
