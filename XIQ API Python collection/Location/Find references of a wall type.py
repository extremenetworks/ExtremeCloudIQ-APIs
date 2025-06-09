import requests
         
baseUrl = 'api.extremecloudiq.com'
wall_type_id = 'The Wall Type ID'
access_token = '***'

url = f"https://{baseUrl}/locations/wall/type/references/{wall_type_id}"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}



response = requests.get(url, headers=headers, params=params)

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
