import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/clients/alias"

payload = json.dumps([
  {
    "mac_address": "mac_address_1",
    "alias": "string"
  },
  {
    "mac_address": "mac_address_2",
    "alias": "string"
  }
])

headers = {
  'Content-Type': 'text/plain',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
