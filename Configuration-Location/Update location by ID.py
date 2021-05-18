import requests
import json

url = "https://api.extremecloudiq.com/locations/{{loc_id}}"

payload = json.dumps({
  "parent_id": "95135",
  "name": "TheLocationName"
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
