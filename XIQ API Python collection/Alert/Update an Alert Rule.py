import requests
         
baseUrl = 'api.extremecloudiq.com'
alert_policy_id = 'Alert Policy ID'
alert_rule_id = 'Alert Rule ID'
access_token = '***'

url = f"https://{baseUrl}/alert-policies/{alert_policy_id}/rules/{alert_rule_id}"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "description": "string",
  "severity_id": 0,
  "trigger_type": "string",
  "duration": 0,
  "time_window": 0,
  "count": 0,
  "threshold": 0,
  "operator": "string"
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
