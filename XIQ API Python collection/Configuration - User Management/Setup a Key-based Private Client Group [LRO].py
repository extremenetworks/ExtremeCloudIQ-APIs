import requests
         
baseUrl = 'https://api.extremecloudiq.com'
access_token = '***'

url = f"{baseUrl}/pcgs/key-based"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "policy_name": "string",
  "ssid_name": "string",
  "users": [
    {
      "name": "string",
      "email": "string",
      "user_group_name": "string"
    }
  ]
}
# async: False (disabled)

response = requests.post(url, headers=headers, params=params)

print("Status Code:", response.status_code)

content_type = response.headers.get('Content-Type')
lro_url = response.headers.get('Location')
if lro_url:
    print(lro_url)
elif content_type and 'application/json' in content_type:
    try:
        print("Response Body:", response.json())
    except ValueError:
        print("Response is not valid JSON")
else:
    print("Content-Type is not application/json")
    print(response.text)
