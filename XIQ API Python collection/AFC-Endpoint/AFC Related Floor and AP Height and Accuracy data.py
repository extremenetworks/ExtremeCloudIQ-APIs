import requests
         
baseUrl = 'https://api.extremecloudiq.com'
access_token = '***'

url = f"{baseUrl}/floor/afc/details"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "floor_id": -88238953,
  "floor_height": 16618431.132390216,
  "floor_height_accuracy": 46095652,
  "ap_height": 47095775.59816691,
  "ap_height_accuracy": -23198528
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
