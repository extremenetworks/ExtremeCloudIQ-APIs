import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/devices/"

payload = json.dumps({
  "ids": [
    0 # List of Device IDs to reboot
  ]
})
headers = {
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
