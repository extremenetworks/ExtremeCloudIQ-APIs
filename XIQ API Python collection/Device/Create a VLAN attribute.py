import requests
import json

device_id = 0 
access_token = '***'

url = f"https://api.extremecloudiq.com/devices/{device_id}/config/vlan-attributes"

payload = json.dumps({
  "name": "string",
  "dhcp_snooping_enabled": True,
  "dhcp_snooping_action": "NONE",
  "igmp_snooping_enabled": True,
  "immediate_leave": True,
  "always_create": True,
  "vlan_id": 0
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
