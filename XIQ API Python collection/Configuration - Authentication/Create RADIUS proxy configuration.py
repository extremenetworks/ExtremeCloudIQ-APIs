import requests
import json

access_token = '***'

url ="https://api.extremecloudiq.com/radius-client-objects"

payload = json.dumps({
  "name": "radius-proxy-1",
  "description": "Radius Proxy 1",
  "format_type": "NAI",
  "retry_count": 3,
  "retry_delay": 5,
  "dead_time": 300,
  "enable_inject_operator_name_attribute": False,
  "device_ids": [
    1
  ],
  "clients": [
    {
      "shared_secret": "123456",
      "description": "",
      "l3_address_profile_id": 1000
    }
  ],
  "realms": [
    {
      "name": "NULL",
      "enable_strip_realm_name": False,
      "radius_client_object_id": 2000
    },
    {
      "name": "DEFAULT",
      "enable_strip_realm_name": False,
      "radius_client_object_id": 3000
    }
  ]
})
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
