import requests
         
baseUrl = 'https://api.extremecloudiq.com'
access_token = '***'

url = f"{baseUrl}/thread/routers"
headers = {'Authorization': f'Bearer {access_token}'}
params = {'page': '1', 'limit': '10', 'ids': '0'}

# sortField:  (disabled)
# sortOrder:  (disabled)
# views:  (disabled)
# fields:  (disabled)

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
