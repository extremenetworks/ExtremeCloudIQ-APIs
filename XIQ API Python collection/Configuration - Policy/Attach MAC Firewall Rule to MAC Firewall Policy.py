import requests
         
mac_firewall_policy_id = 'The MAC Firewall Policy ID'
access_token = '***'

url = f"https://api.extremecloudiq.com/mac-firewall-policies/{mac_firewall_policy_id}/:attach"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "action": "PERMIT",
  "source_mac": 0,
  "destination_mac": 0,
  "logging_type": "OFF"
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
