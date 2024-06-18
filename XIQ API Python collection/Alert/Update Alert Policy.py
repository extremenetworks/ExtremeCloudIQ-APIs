import requests
import json

alert_policy_id = 0
site_ids = [0]
access_token = '***'

url = f"https://api.extremecloudiq.com/alert-policies/{str(alert_policy_id)}"

payload = json.dumps({
  "name": "string",
  "site_ids":
    site_ids
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
