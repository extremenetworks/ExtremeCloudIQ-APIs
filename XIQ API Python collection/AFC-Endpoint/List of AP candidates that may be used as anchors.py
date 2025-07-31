import requests
         
baseUrl = 'https://api.extremecloudiq.com'
owner_id = 'Owner ID'
access_token = '***'

url = f"{baseUrl}/afc/mobileapp/apcandidates"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "owner_id": owner_id,
  "bssid_list": [
    "nostrud nisi officia anim cillum",
    "ut velit"
  ]
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
