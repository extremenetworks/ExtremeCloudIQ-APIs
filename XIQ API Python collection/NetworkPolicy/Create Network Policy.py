import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/network-policies"

payload = json.dumps({
  "name": "string",
  "description": "string",
  "type": "NETWORK_ACCESS_AND_SWITCHING"
})
headers = {
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
