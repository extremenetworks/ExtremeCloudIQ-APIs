import requests
import json

url = "https://api.extremecloudiq.com/users/admin User ID"

payload = json.dumps({
  "login_name": "newlogin1@company.com",
  "display_name": "New Name1",
  "idle_timeout": "30",
  "user_role": "ADMINISTRATIVE_ROLE_OBSERVER"
})
headers = {
  'Authorization': '',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
