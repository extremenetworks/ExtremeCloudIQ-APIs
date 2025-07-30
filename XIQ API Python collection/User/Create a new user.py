import requests
         
baseUrl = 'https://api.extremecloudiq.com'
access_token = '***'

url = f"{baseUrl}/users"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "login_name": "example1@company.com",
  "display_name": "example1",
  "idle_timeout": 30,
  "user_role": "ADMINISTRATOR",
  "location_ids": [
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
