import requests
import json

mac_object_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/mac-object-profiles/{mac_object_id}"

payload = json.dumps({
  "name": "string",
  "description": "string",
  "value": "string",
  "mac_address_end": "string"
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
