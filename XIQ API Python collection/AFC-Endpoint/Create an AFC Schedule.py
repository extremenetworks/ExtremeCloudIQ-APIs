import requests
import json

owner_id = 0
folder_id = 0
access_token = '***'

url = "https://api.extremecloudiq.com/site/afc/schedule"

payload = json.dumps({
  "ownerId": owner_id,
  "folderId": folder_id,
  "siteTimeZone": "string",
  "siteSchedule": 0
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
