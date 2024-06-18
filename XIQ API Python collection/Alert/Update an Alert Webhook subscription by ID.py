import requests
import json

webhook_id = 0
alert_policy_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/alert-subscriptions/webhooks/{str(webhook_id)}"

payload = json.dumps({
  "url": "string",
  "secret": "string",
  "is_enabled": True,
  "is_subscribe_all": True,
  "alert_policy_ids": [
    alert_policy_id
  ]
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
