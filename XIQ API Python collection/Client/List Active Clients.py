import requests
         

access_token = '***'

url = f"https://api.extremecloudiq.com/clients/active"
headers = {'Authorization': f'Bearer {access_token}'}
params = {'page': '1', 'limit': '10', 'views': 'FULL'}

# locationIds: {{floor_id}} (disabled)
# deviceIds: {{device_id}} (disabled)
# vlans: 200 (disabled)
# userProfileNames: Profile Name (disabled)
# ssids: SSID Name (disabled)
# clientOsNames:  (disabled)
# clientConnectionTypes: WIRELESS (disabled)
# clientHealthStatus: POOR (disabled)
# excludeLocallyManaged: false (disabled)
# usernames:  (disabled)
# searchString:  (disabled)
# sortField:  (disabled)
# sortOrder: ASC (disabled)
# fields: id (disabled)

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
