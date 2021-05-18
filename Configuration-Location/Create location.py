import requests
import json

url = "https://api.extremecloudiq.com/locations/"

payload = json.dumps({
  "parent_id": "654321",
  "name": "TheBuildingName",
  "address": "The building street address"
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
