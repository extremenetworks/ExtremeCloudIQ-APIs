import requests
         
baseUrl = 'https://api.extremecloudiq.com'
site_id = 'Site ID'
access_token = '***'

url = f"{baseUrl}/applications/usage/summary/export"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "site_ids": [
    site_id
  ],
  "application_name": [
    "string",
    "string"
  ],
  "category_name": [
    "string",
    "string"
  ],
  "number_filter": [
    {
      "column_name": "string",
      "filter_type": "BTW",
      "value": 3261.174924261927,
      "min": 3189.9477031991673,
      "max": 6409.589795124802
    },
    {
      "column_name": "string",
      "filter_type": "BTW",
      "value": 4598.12648292365,
      "min": 9008.729727404578,
      "max": 7674.647296524881
    }
  ]
}
# sortField: USAGE (disabled)
# order: ASC (disabled)
# name: string (disabled)
# async: false (disabled)

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
