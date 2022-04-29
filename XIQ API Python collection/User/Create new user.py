import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/users"

payload = json.dumps({
  "login_name": "example1@company.com",
  "display_name": "example1",
  "idle_timeout": "30",
  "user_role": "ADMINISTRATOR"
})
headers = {
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
