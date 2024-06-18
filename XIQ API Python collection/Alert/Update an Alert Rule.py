import requests
import json

alert_policy_id = 0
alert_rule_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/alert-policies/{str(alert_policy_id)}/rules/{str(alert_rule_id)}"

payload = json.dumps({
  "description": "string",
  "severity_id": 0,
  "trigger_type": "string",
  "duration": 0,
  "time_window": 0,
  "count": 0,
  "threshold": 0,
  "operator": "string"
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
