import requests
         
webhook_id = 'Webhook Alert Subscription ID'
alert_policy_id = 'Alert Policy ID'
access_token = '***'

url = f"https://api.extremecloudiq.com/alert-subscriptions/webhooks/{webhook_id}"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "url": "string",
  "secret": "string",
  "is_enabled": True,
  "is_subscribe_all": True,
  "alert_policy_ids": [
    alert_policy_id
  ]
}


response = requests.put(url, headers=headers, params=params)

print("Status Code:", response.status_code)

content_type = response.headers.get('Content-Type')
if content_type and 'application/json' in content_type:
    try:
        print("Response Body:", response.json())
    except ValueError:
        print("Response is not valid JSON")
else:
    print("Content-Type is not application/json")
    print(response.text)
