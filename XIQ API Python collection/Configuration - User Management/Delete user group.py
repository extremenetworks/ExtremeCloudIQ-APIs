import requests
import json

group_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/usergroups/{group_id}"

payload={}
headers = {
  'accept': '*/*',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
