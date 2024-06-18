import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/alert-subscriptions/webhooks/:delete"

payload = json.dumps({
  "ids": [
    0
  ]
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
