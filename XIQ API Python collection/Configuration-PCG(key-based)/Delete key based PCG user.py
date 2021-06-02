import requests
import json

url = "https://api.extremecloudiq.com/pcg/key-based/{{pcgk_id}}/users"

payload = json.dumps({
  "user_ids": [
    0
  ]
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
