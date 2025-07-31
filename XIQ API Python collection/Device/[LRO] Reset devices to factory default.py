import requests
         
baseUrl = 'https://api.extremecloudiq.com'
device_id = 'device ID'
access_token = '***'

url = f"{baseUrl}/devices/:reset"
headers = {'Authorization': f'Bearer {access_token}'}
params = {'async': 'false'}
body = {
  "device_ids": [
    device_id
  ]
}


response = requests.post(url, headers=headers, params=params)

print("Status Code:", response.status_code)

content_type = response.headers.get('Content-Type')
lro_url = response.headers.get('Location')
if lro_url:
    print(lro_url)
elif content_type and 'application/json' in content_type:
    try:
        print("Response Body:", response.json())
    except ValueError:
        print("Response is not valid JSON")
else:
    print("Content-Type is not application/json")
    print(response.text)
