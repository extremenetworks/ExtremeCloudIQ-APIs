import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/auth/apitoken"

payload = json.dumps({
  "description": "access_token for read account only",
  "expire_time": 1650999412,
  "permissions": [
    "account:r"
  ]
})
headers = {
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
