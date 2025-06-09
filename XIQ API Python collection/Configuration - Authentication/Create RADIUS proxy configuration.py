import requests
         
baseUrl = 'api.extremecloudiq.com'
device_id = 'device ID'
access_token = '***'

url = f"https://{baseUrl}/radius-proxies"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "name": "radius-proxy-1",
  "description": "Radius Proxy 1",
  "format_type": "NAI",
  "retry_count": 3,
  "retry_delay": 5,
  "dead_time": 300,
  "enable_inject_operator_name_attribute": False,
  "device_ids": [
device_id
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
