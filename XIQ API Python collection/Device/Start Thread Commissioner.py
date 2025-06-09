import requests
         
baseUrl = 'api.extremecloudiq.com'
device_id = 'device ID'
access_token = '***'

url = f"https://{baseUrl}/devices/{device_id}/thread/commissioner/:start"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "device_id": 0,
  "comm_timeout": 2000000,
  "interface_name": "string"
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
