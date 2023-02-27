import requests
import json

radius_proxy_id = 0
access_token = '***'

url =f"https://api.extremecloudiq.com/radius-client-objects/{radius_proxy_id}"

payload = json.dumps({
  "name": "radius-proxy-1",
  "description": "Radius Proxy 1",
  "format_type": "NAI",
  "retry_count": 3,
  "retry_delay": 5,
  "dead_time": 300,
  "enable_inject_operator_name_attribute": False,
  "clients": [
    {
      "id": 1 # The RADIUS client ID, using an existing ID or leave empty to create a new one
    },
    {
      "shared_secret": "123456",
      "description": "",
      "l3_address_profile_id": 1000 # The associate L3 address profile ID
    }
  ],
  "realms": [
    {
      "id": 1 # The RADIUS proxy realm ID, using an existing ID or leave empty to create a new one
    },
    {
      "id": 2 # The RADIUS proxy realm ID, using an existing ID or leave empty to create a new one
    },
    {
      "name": "test-realm",
      "enable_strip_realm_name": False,
      "radius_client_object_id": 3000 # The associate RADIUS client object ID
    }
  ]
})
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
