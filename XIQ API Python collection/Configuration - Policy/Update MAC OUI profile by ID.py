import requests
         
baseUrl = 'api.extremecloudiq.com'
mac_oui_id = 'MAC OUI ID'
access_token = '***'

url = f"https://{baseUrl}/radio-profiles/mac-ouis/{mac_oui_id}"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "name": "string",
  "value": "string",
  "description": "string",
  "mac_type": "string",
  "defender_defined": True
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
