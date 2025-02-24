import requests
         
username = 'username'
password = 'password'
access_token = '***'

url = f"https://api.extremecloudiq.com/login"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "username": "username",
  "password": "password"
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
