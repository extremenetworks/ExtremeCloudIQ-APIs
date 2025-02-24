import requests
         
device_id = 'device ID'
access_token = '***'

url = f"https://api.extremecloudiq.com/devices/radio-information"
headers = {'Authorization': f'Bearer {access_token}'}
params = {'page': '1', 'limit': '10', 'deviceIds': f'{device_id}'}

# includeDisabledRadio: false (disabled)

response = requests.get(url, headers=headers, params=params)

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
