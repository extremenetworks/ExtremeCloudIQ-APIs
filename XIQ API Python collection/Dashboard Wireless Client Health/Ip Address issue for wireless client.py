import requests
         
baseUrl = 'https://api.extremecloudiq.com'
client_mac = 'Client MAC address'
site_id = 'Site ID'
access_token = '***'

url = f"{baseUrl}/dashboard/wireless/client-health/issue/ipaddress"
headers = {'Authorization': f'Bearer {access_token}'}
params = {'page': '1', 'limit': '10', 'macAddress': f'{client_mac}'}
body = {
  "site_ids": [
    site_id
  ]
}
# includeUnassigned: false (disabled)

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
