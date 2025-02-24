import requests
         

access_token = '***'

url = f"https://api.extremecloudiq.com/devices/{{id}}/config/vlan-attributes"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "name": "string",
  "dhcp_snooping_enabled": True,
  "dhcp_snooping_action": "NONE",
  "igmp_snooping_enabled": True,
  "immediate_leave": True,
  "always_create": True,
  "vlan_id": 0
}


response = requests.post(url, headers=headers, params=params)

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
