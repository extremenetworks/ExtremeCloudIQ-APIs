import requests
import json

ip_firewall_policy_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/ip-firewall-policies/{ip_firewall_policy_id}/:attach"

payload = json.dumps({
  "action": "PERMIT",
  "service_id": 0,
  "source_ip_id": 0,
  "destination_ip_id": 0,
  "logging_type": "OFF"
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
