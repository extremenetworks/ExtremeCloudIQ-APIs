import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/devices/:cli?async=true"

payload = json.dumps({
  "devices": {
    "ids": [
      0 # List of IDs to send the CLI commands to
    ]
  },
  "clis": [
    "List of CLI commands as strings"
  ]
})
headers = {
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.headers) # LRO location URL is included in headers
print(response.text)

print(f"Long Running Status URL - {response.headers['Location']}")