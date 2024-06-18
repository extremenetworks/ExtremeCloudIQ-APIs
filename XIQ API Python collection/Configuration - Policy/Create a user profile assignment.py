import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/user-profile-assignments"

payload = json.dumps({
  "name": "string",
  "description": "string",
  "folder_ids": [
    0
  ],
  "assignment_radius_attribute": {
    "attribute_type": "TUNNEL",
    "attribute_values": "string"
  }
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
