import requests
         
baseUrl = 'api.extremecloudiq.com'
hotspot_service_provider_id = 'Hotspot Service Provider profile ID'
access_token = '***'

url = f"https://{baseUrl}/hotspot-service-provider-profiles/{hotspot_service_provider_id}"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}



response = requests.delete(url, headers=headers, params=params)

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
