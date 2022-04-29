import requests
import json

radius_id = 0
access_token = '***'

url =f"https://api.extremecloudiq.com/radius-client-objects/{radius_id}"

payload = json.dumps({
  "name": "string",
  "description": "string",
  "enable_inject_operator_name_attribute": True,
  "enable_message_authenticator_attribute": True,
  "enable_permit_dynamic_authorization_message_change": True,
  "retry_interval": 0,
  "accounting_interim_update_interval": 0
})
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
