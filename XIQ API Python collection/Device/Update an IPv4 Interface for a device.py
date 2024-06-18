import requests
import json

device_id = 0
ipv4IntId = 0 
access_token = '***'

url = f"https://api.extremecloudiq.com/devices/{device_id}/config/vlan-ipv4-intf/{ipv4IntId}"

payload = json.dumps({
  "ip_address": "string",
  "routing_instance": "string",
  "enable_forwarding": True,
  "enable_vlan_loopback": True,
  "use_ip_addr_as_ospf_router_id": True,
  "override_dhcp_relay": True,
  "enable_dhcp": True,
  "primary_dhcp_server": "string",
  "secondary_dhcp_server": "string",
  "predefined": True,
  "subnetwork_id": 0,
  "vlan_id": 0
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("PATCH", url, headers=headers, data=payload)

print(response.text)
