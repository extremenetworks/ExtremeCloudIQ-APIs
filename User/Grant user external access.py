import requests
import json

url = "https://api.extremecloudiq.com/users/externalaccess"

payload = json.dumps({
  "login_name": "example1@company.com",
  "user_role": "ADMINISTRATIVE_ROLE_ADMINISTRATOR"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
