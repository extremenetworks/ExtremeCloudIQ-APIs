import requests
import json

mac_firewall_policy_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/mac-firewall-policies/{mac_firewall_policy_id}/:attach"

payload = json.dumps({
  "action": "PERMIT",
  "source_mac": 0,
  "destination_mac": 0,
  "logging_type": "OFF"
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
