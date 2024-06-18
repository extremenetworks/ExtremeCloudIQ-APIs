import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/network-services"

payload = json.dumps({
  "name": "string",
  "description": "string",
  "ip_protocol": "TCP",
  "protocol_number": 0,
  "port_number": 0,
  "alg_type": "NONE"
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
