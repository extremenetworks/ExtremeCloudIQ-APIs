import requests
         
baseUrl = 'api.extremecloudiq.com'
user_id = 'User ID'
group_id = 'User Group ID'
access_token = '***'

url = f"https://{baseUrl}/endusers/{user_id}"
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
