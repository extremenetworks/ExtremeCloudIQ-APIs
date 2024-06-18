import requests
import json

url = "https://api.extremecloudiq.com/alerts/:acknowledge"

payload = json.dumps({
  "alert_ids": [
    "string"
  ]
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
