import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/radio-profiles/mac-ouis"

payload = json.dumps({
  "name": "string",
  "value": "string",
  "description": "string",
  "mac_type": "string",
  "defender_defined": True
})
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
