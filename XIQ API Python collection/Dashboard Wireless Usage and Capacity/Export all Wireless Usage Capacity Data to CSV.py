import requests
         
baseUrl = 'api.extremecloudiq.com'
site_id = 'Site ID'
device_id = 'device ID'
building_id = 'Building ID'
access_token = '***'

url = f"https://{baseUrl}/dashboard/wireless/usage-capacity/export"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "site_ids": [
    site_id
  ],
  "device_ids": [
    device_id
  ],
  "building_ids": [
    building_id
  ],
  "buildings": [
    "string"
  ],
  "floors": [
    "string"
  ],
  "has_usage_capacity_issues": True,
  "number_filters": [
    {
      "column_name": "string",
      "filter_type": "GT",
      "value": 0,
      "min": 0,
      "max": 0
    }
  ],
  "has_packet_loss_issues": True,
  "has_retries_issues": True
}
# keyword: None (disabled)
# sortField: None (disabled)
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
