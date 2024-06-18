import requests

alert_policy_id = 0
alert_rule_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/alert-policies/{str(alert_policy_id)}/rules/{str(alert_rule_id)}/:disable"

payload = {}
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
