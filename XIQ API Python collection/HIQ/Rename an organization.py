import requests
import json

org_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/hiq/organizations/{org_id}/:rename"

payload = json.dumps("new name")
headers = {
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
