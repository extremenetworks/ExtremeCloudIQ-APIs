import requests
import json

mac_oui_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/radio-profiles/mac-ouis/{mac_oui_id}"

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

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
