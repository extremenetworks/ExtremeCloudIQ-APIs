import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/hiq/context/reading"

payload = json.dumps([
  0
])
headers = {
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
