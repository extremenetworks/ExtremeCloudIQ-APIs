import requests
         

access_token = '***'

url = f"https://api.extremecloudiq.com/vlan-profiles"
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
