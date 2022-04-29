import requests
import json

user_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/endusers/{user_id}"

payload = json.dumps({
  "user_group_id": "987654321",
  "name": "MyName1",
  "user_name": "EnterNewOrUseSameAsEmailPhoneOrName",
  "description": "AShortDescription",
  "organization": "TheOrganizationName",
  "visit_purpose": "PurposeForTheVisit",
  "password": "XzwtxpmWsDuxSmSqrX",
  "email_address": "user1@mailserver.com",
  "phone_number": "14082147380",
  "email_password_delivery": "user1@mailserver.com",
  "sms_password_delivery": "14082147380"
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
