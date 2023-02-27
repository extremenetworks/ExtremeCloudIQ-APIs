import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/devices/network-policy/:revoke"

payload = json.dumps({
  "ids": [
    0 # List of Device IDs to revoke Network Policy
  ]
})
headers = {
  'accept': '*/*',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
