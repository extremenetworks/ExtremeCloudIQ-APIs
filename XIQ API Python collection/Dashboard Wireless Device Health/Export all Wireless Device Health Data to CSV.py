import requests
         
baseUrl = 'https://api.extremecloudiq.com'
site_id = 'Site ID'
device_id = 'device ID'
access_token = '***'

url = f"{baseUrl}/dashboard/wireless/device-health/export"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "site_ids": [
    site_id
  ],
  "device_ids": [
    device_id
  ],
  "has_device_health_issues": True,
  "number_filter": [
    {
      "column_name": "string",
      "filter_type": "GT",
      "value": 0,
      "min": 0,
      "max": 0
    }
  ]
}
# keyword:  (disabled)
# sortField:  (disabled)
# sortOrder: ASC (disabled)
# unassigned_devices: false (disabled)

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
