import requests
         
baseUrl = 'api.extremecloudiq.com'
access_token = '***'

url = f"https://{baseUrl}/user-profile-assignments"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "name": "string",
  "description": "string",
  "folder_ids": [
    0
  ],
  "assignment_radius_attribute": {
    "attribute_type": "TUNNEL",
    "attribute_values": "string"
  }
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
