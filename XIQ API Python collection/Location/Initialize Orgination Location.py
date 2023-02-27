import requests
import json

access_token = '***'

country = "AFGHANISTAN_4"
url = "https://api.extremecloudiq.com/locations/:init"

payload = json.dumps({
  "organization": "string",
  "country": country
})
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
