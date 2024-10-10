import requests
import json

device_id = 0
access_token = '***'

url = "https://api.extremecloudiq.com/aps/afc/update"


payload = json.dumps({
  "ids": [
    device_id
  ]
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
