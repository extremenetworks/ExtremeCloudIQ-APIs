import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/usergroups?page=1&limit=10"

payload={}
headers = {
  'accept': '*/*',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
