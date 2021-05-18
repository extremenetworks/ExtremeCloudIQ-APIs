import requests
import json

url = "https://api.extremecloudiq.com/users/externalaccess/{{uid}}"

payload = json.dumps({
  "user_role": "ADMINISTRATIVE_ROLE_ADMINISTRATOR"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
