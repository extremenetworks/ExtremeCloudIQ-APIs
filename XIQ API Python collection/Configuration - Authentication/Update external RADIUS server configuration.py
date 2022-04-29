import requests
import json

ex_radius_id = 0
access_token = '***'

url =f"https://api.extremecloudiq.com/radius-servers/external/{ex_radius_id}"

payload = json.dumps({
  "name": "string",
  "shared_secret": "string",
  "authentication_port": 0,
  "accounting_port": 0,
  "server_type": "BOTH",
  "ip_addr": "string"
})
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
