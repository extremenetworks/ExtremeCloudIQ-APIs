import requests
         
baseUrl = 'api.extremecloudiq.com'
loc_id = 'Location ID'
access_token = '***'

url = f"https://{baseUrl}/locations"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "parent_id": "loc_id",
  "name": "Location Name"
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
