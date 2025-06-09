import requests
         
baseUrl = 'api.extremecloudiq.com'
access_token = '***'

url = f"https://{baseUrl}/dashboard/wired/client-health/grid"
headers = {'Authorization': f'Bearer {access_token}'}
params = {'page': '1', 'limit': '10'}
body = {
  "site_ids": [
    0
  ],
  "device_ids": [
    0
  ],
  "filter_field": [
    "IP_CONNECTIVITY_ISSUES_SELF_ASSIGNED_IP"
  ]
}
# keyword: string (disabled)
# sortField: TOTAL_CONGESTION (disabled)
# sortOrder: DESC (disabled)

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
