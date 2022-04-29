import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/pcgs/key-based"

payload = json.dumps({
  "policy_name": "0",
  "ssid_name": "0",
  "users": [
    {
      "name": "0",
      "email": "0",
      "user_group_name": "0"
    }
  ]
})
headers = {
  'accept': '*/*',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
