import requests
         
baseUrl = 'api.extremecloudiq.com'
vlan_id = 'VLAN Profile ID'
access_token = '***'

url = f"https://{baseUrl}/vlan-profiles/{vlan_id}"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "name": "string",
  "default_vlan_id": 0,
  "enable_classification": True,
  "classified_entries": [
    {
      "vlan_id": 0,
      "classification_rule_id": 0
    }
  ]
}


response = requests.patch(url, headers=headers, params=params)

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
