import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/hiq/organizations"

payload = json.dumps({
  "name": "string",
  "color": "string"
})
headers = {
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
