import requests
import json

site_ids = [0]
access_token = '***'

url = "https://api.extremecloudiq.com/alert-policies"

payload = json.dumps({
  "name": "string",
  "site_ids": site_ids
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
