import requests
import json

np_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/pcgs/key-based/network-policy{np_id}/users"

payload = "{\n  \"user_ids\": [\n    ***\n  ]\n}"
headers = {
  'accept': '*/*',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
