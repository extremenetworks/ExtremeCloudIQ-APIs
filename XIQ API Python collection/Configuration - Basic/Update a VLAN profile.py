import requests
import json

vp_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/vlan-profiles/{vp_id}"

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

response = requests.request("PATCH", url, headers=headers, data=payload)

print(response.text)
