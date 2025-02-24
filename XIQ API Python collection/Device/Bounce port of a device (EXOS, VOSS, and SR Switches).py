import requests
         
device_id = 'device ID'
access_token = '***'

url = f"https://api.extremecloudiq.com/devices/{device_id}/bounce-port"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "device_id": device_id,
  "port_number": "6",
  "bounce_port_reason": "string"
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
