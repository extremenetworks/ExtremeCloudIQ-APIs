import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/mac-object-profiles"

payload = json.dumps({
  "name": "string",
  "description": "string",
  "value": "string",
  "mac_type": "MAC_OUI",
  "mac_address_end": "string"
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
