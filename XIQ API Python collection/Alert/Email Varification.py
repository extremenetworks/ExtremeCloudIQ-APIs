import requests
         
baseUrl = 'api.extremecloudiq.com'
email_id = 'Email Alert Subscription ID'
alert_policy_id = 'Alert Policy ID'
access_token = '***'

url = f"https://{baseUrl}/alert-subscriptions/emails/{email_id}/:verify"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "email": "string",
  "is_enabled": True,
  "is_subscribe_all": True,
  "alert_policy_ids": [
    alert_policy_id
  ]
}


response = requests.post(url, headers=headers, params=params)

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
