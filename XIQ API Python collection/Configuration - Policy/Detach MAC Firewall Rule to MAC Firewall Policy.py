import requests
import json

mac_firewall_policy_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/mac-firewall-policies/{mac_firewall_policy_id}/:detach"

payload = json.dumps(0)
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
