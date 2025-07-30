import requests
         
baseUrl = 'https://api.extremecloudiq.com'
afcdetail_id = 'AFC Detail ID'
owner_id = 'Owner ID'
access_token = '***'

url = f"{baseUrl}/floor/afc/details/{afcdetail_id}"
headers = {'Authorization': f'Bearer {access_token}'}
params = {'ownerId': f'{owner_id}'}



response = requests.delete(url, headers=headers, params=params)

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
