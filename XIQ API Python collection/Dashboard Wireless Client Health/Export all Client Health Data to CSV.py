import requests
         
site_id = 'Site ID'
device_id = 'device ID'
access_token = '***'

url = f"https://api.extremecloudiq.com/dashboard/wireless/client-health/export"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "site_ids": [
    site_id
  ],
  "device_ids": [
    device_id
  ],
  "number_filter": [
    {
      "column_name": "string",
      "filter_type": "GT",
      "value": 0,
      "min": 0,
      "max": 0
    }
  ],
  "alias": [
    "string"
  ],
  "auth_methods": [
    "string"
  ],
  "encryption_methods": [
    "string"
  ],
  "operating_systems": [
    "string"
  ],
  "ssids": [
    "string"
  ],
  "user_profiles": [
    "string"
  ],
  "frequency": [
    "string"
  ],
  "category_assignments": [
    "string"
  ],
  "has_authentication_issues": True,
  "has_association_issues": True,
  "has_ip_address_issues": True,
  "has_roaming_issues": True,
  "is_client_unhealthy": True
}
# keyword:  (disabled)
# connectionStatus: CONNECTED (disabled)
# sortField:  (disabled)
# sortOrder: ASC (disabled)

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
