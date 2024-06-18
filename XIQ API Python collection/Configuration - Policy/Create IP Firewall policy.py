import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/ip-firewall-policies"

payload = json.dumps({
  "name": "string",
  "description": "string",
  "rules": [
    {
      "action": "PERMIT",
      "service_id": 0,
      "source_ip_id": 0,
      "destination_ip_id": 0,
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
