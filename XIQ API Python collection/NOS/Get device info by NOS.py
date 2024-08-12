import requests
import json

device_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/nos/device/{device_id}/nos-api"

payload = json.dumps({
  "endpoint": "string",
  "method": "GET",
  "json_body": [
    "string"
  ]
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
