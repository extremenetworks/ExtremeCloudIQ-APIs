import requests
         
baseUrl = 'api.extremecloudiq.com'
site_id = 'Site ID'
access_token = '***'

url = f"https://{baseUrl}/devices/rm-devices-page"
headers = {'Authorization': f'Bearer {access_token}'}
params = {'page': '1', 'limit': '10'}
body = {
  "site_ids": [
    site_id
  ],
  "sns": [
    "string"
  ],
  "mac_addresses": [
    "string"
  ],
  "hostnames": [
    "string"
  ],
  "default_gateway_ips": [
    "string"
  ],
  "product_types": [
    "string"
  ],
  "firmware_versions": [
    "string"
  ],
  "country_codes": [
    0
  ],
  "managed_by": [
    "string"
  ]
}
# keyword: None (disabled)
# connected: true (disabled)
# adminStates: NEW (disabled)
# deviceCategory: WIRELESS (disabled)
# sortField: HOSTNAME (disabled)
# order: ASC (disabled)
# deviceTypes: REAL (disabled)
# configMismatch: True (disabled)
# async: false (disabled)

response = requests.post(url, headers=headers, params=params)

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
