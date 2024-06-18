import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/l3-address-profiles"

payload = json.dumps({
  "name": "string",
  "description": "string",
  "value": "string",
  "address_type": "IP_ADDRESS",
  "enable_classification": True,
  "classified_entries": [
    {
      "class_asgn_id": 0,
      "value": "string",
      "description": "string",
      "netmask": "string",
      "ip_address_end": "string",
      "wildcard_mask": "string"
    }
  ],
  "ip_address_end": "string",
  "netmask": "string",
  "wildcard_mask": "string"
})

headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
