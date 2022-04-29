import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/vlan-profiles"

payload = json.dumps({
  "name": "string",
  "default_vlan_id": 0,
  "enable_classification": True,
  "classified_entries": [
    {
      "vlan_id": 0,
      "classification_rule_id": 0
    }
  ]
})
headers = {
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
