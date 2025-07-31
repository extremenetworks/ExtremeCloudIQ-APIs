import requests
         
baseUrl = 'https://api.extremecloudiq.com'
group_id = 'User Group ID'
access_token = '***'

url = f"{baseUrl}/endusers"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "user_group_id": group_id,
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
