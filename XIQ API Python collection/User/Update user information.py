import requests
import json

user_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/users/{user_id}"

payload = json.dumps({
  "login_name": "newlogin1@company.com",
  "display_name": "New Name1",
  "idle_timeout": "30",
  "user_role": "OBSERVER"
})
headers = {
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("PATCH", url, headers=headers, data=payload)

print(response.text)
