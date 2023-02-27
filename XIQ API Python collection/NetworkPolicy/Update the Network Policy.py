import requests
import json

np_id = 0 # Network Policy ID
access_token = '***'

url = f"https://api.extremecloudiq.com/network-policies/{np_id}"

payload = json.dumps({
  "name": "string",
  "description": "string",
  "type": "NETWORK_ACCESS_AND_SWITCHING"
})
headers = {
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
