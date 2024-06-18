import requests
import json

device_id = 0
vlan_profile_id = 0 
access_token = '***'

url = f"https://api.extremecloudiq.com/devices/{device_id}/config/vlan-attributes/{vlan_profile_id}"

payload = json.dumps({
  "name": "string",
  "dhcp_snooping_enabled": True,
  "dhcp_snooping_action": "NONE",
  "igmp_snooping_enabled": True,
  "immediate_leave": True,
  "always_create": True
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("PATCH", url, headers=headers, data=payload)

print(response.text)
