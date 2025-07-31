import requests
         
baseUrl = 'https://api.extremecloudiq.com'
np_id = 'Network Policy ID'
access_token = '***'

url = f"{baseUrl}/pcgs/key-based/network-policy-{np_id}/port-assignments"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "port_assignments": [
    {
      "device_id": 0,
      "eth1_user_id": 0,
      "eth2_user_id": 0,
      "eth3_user_id": 0
    }
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
