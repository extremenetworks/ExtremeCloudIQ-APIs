import requests
         
baseUrl = 'https://api.extremecloudiq.com'
site_id = 'Site ID'
access_token = '***'

url = f"{baseUrl}/alert-policies"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "name": "string",
  "site_ids": [
    site_id
  ]
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
