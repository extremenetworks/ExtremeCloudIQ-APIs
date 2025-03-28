import requests
         

access_token = '***'

url = f"https://api.extremecloudiq.com/credential-distribution-groups"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "name": "string",
  "enable_email_approval": True,
  "enable_user_limitation": True,
  "employee_group_type": "ADMIN",
  "employee_groups": [
    {
      "name": "string"
    }
  ],
  "restrict_number": 0,
  "user_group_ids": [
    0
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
