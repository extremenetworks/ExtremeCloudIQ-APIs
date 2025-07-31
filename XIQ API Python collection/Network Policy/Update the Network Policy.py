import requests
         
baseUrl = 'https://api.extremecloudiq.com'
np_id = 'Network Policy ID'
access_token = '***'

url = f"{baseUrl}/network-policies/{np_id}"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "name": "string",
  "description": "string",
  "type": "NETWORK_ACCESS_AND_SWITCHING"
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
