import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/devices/:cli"

payload = json.dumps({
  "devices": {
    "ids": [
      0
    ]
  },
  "clis": [
    "string"
  ]
})
headers = {
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
