import requests
import json

url = "https://api.extremecloudiq.com/locations/building"

payload = json.dumps({
  "parent_id": "95135",
  "name": "TheLocationName"
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
