import requests
         
baseUrl = 'api.extremecloudiq.com'
site_id = 'Site ID'
access_token = '***'

url = f"https://{baseUrl}/dashboard/sites-with-issues"
headers = {'Authorization': f'Bearer {access_token}'}
params = {'page': '1', 'limit': '10'}
body = {
  "site_ids": [
    site_id
  ]
}
# sortField: Alerts (disabled)
# sortOrder: ASC (disabled)
# keyword:  (disabled)

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
