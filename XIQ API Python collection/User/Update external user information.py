import requests
import json

ex_user_id = 0 
access_token = '***'

url = f"https://api.extremecloudiq.com/users/external/{ex_user_id}"

payload = json.dumps({
  "user_role": "OPERATOR",
  "enable_api_access": True
})
headers = {
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("PATCH", url, headers=headers, data=payload)

print(response.text)
