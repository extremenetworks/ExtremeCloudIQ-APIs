import requests
         
baseUrl = 'api.extremecloudiq.com'
access_token = '***'

url = f"https://{baseUrl}/iot-profiles"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "name": "string",
  "app_id": "THREAD_GATEWAY",
  "thread_gateway": {
    "short_pan_id": "stri",
    "ext_pan_id": "stringstringstri",
    "master_key": "stringstringstringstringstringst",
    "network_name": "string",
    "channel": 0,
    "comm_credentials": "string",
    "comm_timeout": 2000000,
    "enable_nat64": True,
    "white_list": [
      {
        "long_eui": "string",
        "pskd": "string"
      }
    ]
  }
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
