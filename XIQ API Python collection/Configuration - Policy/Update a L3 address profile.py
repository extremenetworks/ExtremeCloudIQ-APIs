import requests
import json

l3_address_profile = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/l3-address-profiles/{l3_address_profile}"

payload = json.dumps({
  "name": "string",
  "description": "string",
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

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
