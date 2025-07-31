import requests
         
baseUrl = 'https://api.extremecloudiq.com'
device_id = 'device ID'
access_token = '***'

url = f"{baseUrl}/devices/{device_id}/mobileapp/gps"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "gps_anchor": False,
  "distance": -1749875.560151711,
  "cep": 97506105.06489238,
  "coordinates": {
    "latitude": -93744182.88722959,
    "longitude": 28834583.110948622,
    "ts": -93844501,
    "source": "APP"
  }
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
