import requests
import json

url = "https://api.extremecloudiq.com/devices/client-monitor/:revoke"

payload = json.dumps({
  "ids": [
    0
  ]
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
