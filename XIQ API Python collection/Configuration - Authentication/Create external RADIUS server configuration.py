import requests
         
baseUrl = 'https://api.extremecloudiq.com'
access_token = '***'

url = f"{baseUrl}/radius-servers/external"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "name": "string",
  "shared_secret": "string",
  "authentication_port": 1812,
  "accounting_port": 1813,
  "server_type": "BOTH",
  "ip_addr": "string",
  "enable_a3": True
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
