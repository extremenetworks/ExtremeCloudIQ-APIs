import requests
         
baseUrl = 'api.extremecloudiq.com'
ex_radius_id = 'The ID for external RADIUS server'
access_token = '***'

url = f"https://{baseUrl}/radius-servers/external/{ex_radius_id}"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}



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
