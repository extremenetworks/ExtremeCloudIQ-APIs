import requests
import json

url = "https://api.extremecloudiq.com/pcg/key-based/{{pcgk_id}}/users"

payload = json.dumps({
  "users": [
    {
      "name": "string",
      "email": "string",
      "user_group_name": "string"
    }
  ]
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
