import requests
         
baseUrl = 'https://api.extremecloudiq.com'
tunnel_conc_id = 'Tunnel Concentrator ID'
access_token = '***'

url = f"{baseUrl}/tunnel-concentrators/{tunnel_conc_id}"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
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
}


response = requests.put(url, headers=headers, params=params)

print("Status Code:", response.status_code)

content_type = response.headers.get('Content-Type')
if content_type and 'application/json' in content_type:
    try:
        print("Response Body:", response.json())
    except ValueError:
        print("Response is not valid JSON")
else:
    print("Content-Type is not application/json")
    print(response.text)
