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
      "id": 1
    },
    {
      "shared_secret": "123456",
      "description": "",
      "l3_address_profile_id": 1000
    }
  ],
  "realms": [
    {
      "id": 1
    },
    {
      "id": 2
    },
    {
      "name": "test-realm",
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

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
