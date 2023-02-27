import requests
import json

loc_id = 0
parent_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/locations/{loc_id}"

payload = json.dumps({
  "parent_id": str(parent_id),
  "name": "TheLocationName"
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
