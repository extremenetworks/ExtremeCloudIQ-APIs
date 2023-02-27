import requests
import json

user_group_id = 0
access_token = '***'

url = "https://api.extremecloudiq.com/endusers"

payload = json.dumps({
  "user_group_id": user_group_id,
  "name": "string",
  "user_name": "string",
  "organization": "string",
  "visit_purpose": "string",
  "description": "string",
  "email_address": "string",
  "phone_number": "string",
  "password": "string",
  "email_password_delivery": "string",
  "sms_password_delivery": "string"
})

headers = {
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
