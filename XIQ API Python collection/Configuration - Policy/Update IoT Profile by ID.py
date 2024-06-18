import requests
import json

iot_profile_id = 0 
access_token = '***'

url = f"https://api.extremecloudiq.com/iot-profiles/{iot_profile_id}"

payload = json.dumps({
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
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
