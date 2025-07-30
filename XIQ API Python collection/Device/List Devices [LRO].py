import requests
         
baseUrl = 'https://api.extremecloudiq.com'
access_token = '***'

url = f"{baseUrl}/devices"
headers = {'Authorization': f'Bearer {access_token}'}
params = {'page': '1', 'limit': '50', 'views': 'FULL'}

# locationId: {{floor_id}} (disabled)
# connected: true (disabled)
# adminStates: MANAGED (disabled)
# macAddresses:  (disabled)
# sns:  (disabled)
# hostnames:  (disabled)
# sortField: SN (disabled)
# order: ASC (disabled)
# fields: ID (disabled)
# deviceTypes: REAL (disabled)
# locationIds: [{{floor_id}}] (disabled)
# nullField: LOCATION_ID (disabled)
# async: false (disabled)
# configMismatch: true (disabled)

response = requests.get(url, headers=headers, params=params)

print("Status Code:", response.status_code)

content_type = response.headers.get('Content-Type')
lro_url = response.headers.get('Location')
if lro_url:
    print(lro_url)
elif content_type and 'application/json' in content_type:
    try:
        print("Response Body:", response.json())
    except ValueError:
        print("Response is not valid JSON")
else:
    print("Content-Type is not application/json")
    print(response.text)
