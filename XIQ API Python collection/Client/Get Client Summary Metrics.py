import requests
         
baseUrl = 'api.extremecloudiq.com'
access_token = '***'

url = f"https://{baseUrl}/clients/summary"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}

# locationIds: {{floor_id}} (disabled)
# deviceIds: {{device_id}} (disabled)
# vlans: 92 (disabled)
# userProfileNames: Profile Name (disabled)
# ssids: SSID Name (disabled)
# clientOsNames:  (disabled)
# clientHealthStatus: POOR (disabled)
# excludeLocallyManaged: false (disabled)
# searchString:  (disabled)

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
