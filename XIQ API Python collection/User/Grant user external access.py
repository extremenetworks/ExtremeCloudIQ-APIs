import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/users/external"

payload = json.dumps({
  "login_name": "example1@company.com",
  "user_role": "ADMINISTRATOR"
})
headers = {
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
