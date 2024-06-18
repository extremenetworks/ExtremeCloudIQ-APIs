import requests
import json

device_id = 0
ipv4StaticRouteId = 0 
access_token = '***'

url = f"https://api.extremecloudiq.com/devices/{device_id}/config/vlan-ipv4-static/{ipv4StaticRouteId}"

payload = json.dumps({
  "name": "string",
  "dest_subnetwork": "string",
  "next_hop_ip": "string",
  "next_hop_ip_ping_protection": True,
  "metric": 0,
  "routing_instance": "string",
  "predefined": True,
  "ipv4_static_route_id": 0
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("PATCH", url, headers=headers, data=payload)

print(response.text)
