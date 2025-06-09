import requests
         
baseUrl = 'api.extremecloudiq.com'
building_id = 'Building ID'
floor_id = 'Floor ID '
client_mac = 'Client MAC address'
access_token = '***'

url = f"https://{baseUrl}/essentials/eloc/clients/{client_mac}/last-known-location"
headers = {'Authorization': f'Bearer {access_token}'}
params = {'floorId': f'{floor_id}', 'parentId': f'{building_id}'}



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
