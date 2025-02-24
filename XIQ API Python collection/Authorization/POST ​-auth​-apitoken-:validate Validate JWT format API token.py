import requests
         
jwttoken = ''
access_token = '***'

url = f"https://api.extremecloudiq.com/auth/apitoken/:validate"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = jwttoken


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
