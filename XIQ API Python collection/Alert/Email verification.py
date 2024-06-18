import requests
import json

email_id = 0
alert_policy_id = 0
email_address = 'string'
access_token = '***'

url = f"https://api.extremecloudiq.com/alert-subscriptions/emails/{str(email_id)}/:verify"

payload = json.dumps({
  "email": email_address,
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

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
