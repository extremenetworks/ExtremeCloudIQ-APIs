import requests
         
baseUrl = 'https://api.extremecloudiq.com'
ssid_id = 'SSID ID'
access_token = '***'

url = f"{baseUrl}/ssids/{ssid_id}/psk/password"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = "string"


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
