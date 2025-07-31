import requests
         
baseUrl = 'https://api.extremecloudiq.com'
access_token = '***'

url = f"{baseUrl}/radsec-proxies"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "name": "radsec-proxy-1",
  "description": "RADSEC Proxy 1",
  "format_type": "WBAID",
  "enable_inject_operator_name_attribute": False,
  "operator_name_type": "WBAID",
  "operator_name": "SP.Extreme:CA",
  "realms": [
    {
      "name": "NULL",
      "enable_strip_realm_name": False,
      "external_radius_server_object_ids": [
        3000,
        3001
      ]
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
