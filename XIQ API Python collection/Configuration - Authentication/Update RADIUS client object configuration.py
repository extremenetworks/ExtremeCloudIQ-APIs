import requests
         
radius_id = 'The ID of RADIUS client object'
access_token = '***'

url = f"https://api.extremecloudiq.com/radius-client-objects/{radius_id}"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "name": "string",
  "description": "string",
  "enable_inject_operator_name_attribute": True,
  "enable_message_authenticator_attribute": True,
  "enable_permit_dynamic_authorization_message_change": True,
  "retry_interval": 100000000,
  "accounting_interim_update_interval": 100000000
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
