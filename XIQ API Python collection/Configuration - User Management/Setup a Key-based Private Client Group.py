import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/pcgs/key-based"

payload = json.dumps({
  "policy_name": "string",
  "ssid_name": "string",
  "users": [
    {
      "name": "string",
      "email": "string",
      "user_group_name": "string"
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
