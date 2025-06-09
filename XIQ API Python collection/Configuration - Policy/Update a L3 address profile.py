import requests
         
baseUrl = 'api.extremecloudiq.com'
l3_address_profile = 'The L3 address profile ID'
access_token = '***'

url = f"https://{baseUrl}/l3-address-profiles/{l3_address_profile}"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "name": "string",
  "description": "string",
  "enable_classification": True,
  "classified_entries": [
    {
      "class_asgn_id": 0,
      "value": "string",
      "description": "string",
      "netmask": "string",
      "ip_address_end": "string",
      "wildcard_mask": "string"
    }
  ],
  "ip_address_end": "string",
  "netmask": "string",
  "wildcard_mask": "string"
}


response = requests.put(url, headers=headers, params=params)

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
