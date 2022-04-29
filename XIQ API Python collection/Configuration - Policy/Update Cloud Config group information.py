import requests
import json

ccg_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/ccgs/{ccg_id}"

payload = json.dumps({
  "name": "string",
  "description": "Update CCG device list",
  "device_ids": [
    0
  ]
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
