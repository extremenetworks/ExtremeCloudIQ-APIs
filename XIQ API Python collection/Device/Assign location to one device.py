import requests
         
baseUrl = 'api.extremecloudiq.com'
device_id = 'device ID'
floor_id = 'Floor ID '
access_token = '***'

url = f"https://{baseUrl}/devices/{device_id}/location"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
    "location_id":floor_id,
    "x":10,
    "y":10,
    "latitude":null,
    "longitude":null
    
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
