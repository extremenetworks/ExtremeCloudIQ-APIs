import requests
         
baseUrl = 'https://api.extremecloudiq.com'
access_token = '***'

url = f"{baseUrl}/copilot/anomalies/exclude-vlans"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "excluded_vlan_details": [
    {
      "vlan_ids": [
        0
      ],
      "site_ids": [
        0
      ]
    }
  ],
  "old_vlan_id": 0,
  "action_type": "ADD",
  "dismiss": True
}


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
