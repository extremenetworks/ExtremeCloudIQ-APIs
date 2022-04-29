import requests
import json

access_token = '***'

url ="https://api.extremecloudiq.com/radius-servers/external"

payload = json.dumps({
  "name": "string",
  "shared_secret": "string",
  "authentication_port": 0,
  "accounting_port": 0,
  "server_type": "BOTH",
  "ip_addr": "string",
  "enable_a3": True
})
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
