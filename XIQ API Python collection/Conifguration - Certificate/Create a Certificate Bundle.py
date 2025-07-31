import requests
         
baseUrl = 'https://api.extremecloudiq.com'
access_token = '***'

url = f"{baseUrl}/certificate-bundles"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "bundle_type": "TRUST_POINT",
  "certificate_ids": [
    -53420604,
    -8801132
  ],
  "name": "consequat voluptate quis exercita",
  "description": "sunt reprehenderit amet nostrud"
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
