import requests
         
baseUrl = 'api.extremecloudiq.com'
access_token = '***'

url = f"https://{baseUrl}/logs/email"
headers = {'Authorization': f'Bearer {access_token}'}
params = {'page': '1', 'limit': '10'}

# username: User Name (disabled)
# startTime: {{myStartTime}} (disabled)
# endTime: {{myEndTime}} (disabled)

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
