import requests
         
baseUrl = 'https://api.extremecloudiq.com'
access_token = '***'
folderId = 0

url = f"{baseUrl}/user-folder-preferences/{folderId}"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "data": {
    "excellent": -90,
    "good": -72,
    "medium": -67,
    "poor": -30
  },
  "type": "string"
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
