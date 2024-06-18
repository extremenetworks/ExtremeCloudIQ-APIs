import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/mac-firewall-profiles"

payload = json.dumps({
  "name": "string",
  "description": "string",
  "rules": [
    {
      "action": "PERMIT",
      "source_mac": 0,
      "destination_mac": 0,
      "logging_type": "OFF"
    }
  ]
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
