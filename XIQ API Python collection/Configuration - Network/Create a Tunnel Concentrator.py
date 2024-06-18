import requests
import json

url = "https://api.extremecloudiq.com/tunnel-concentrators"

payload = json.dumps({
  "name": "string",
  "description": "string",
  "redundant": True,
  "primary_tc": 0,
  "backup_tc": 0,
  "primary_listening_interface": 4,
  "backup_listening_interface": 4,
  "primary_bridging_interface": 4,
  "backup_bridging_interface": 4,
  "primary_ip": "string",
  "backup_ip": "string",
  "primary_vlan": 4094,
  "backup_vlan": 4094,
  "primary_tagged": True,
  "backup_tagged": True,
  "tunnel_address": "string",
  "router_id": 0,
  "gateway": "string",
  "native_vlan": 4094
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
