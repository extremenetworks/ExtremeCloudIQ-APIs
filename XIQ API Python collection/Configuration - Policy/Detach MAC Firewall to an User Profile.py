import requests
         
user_profile_id = 'User Profile ID'
mac_firewall_policy_id = 'The MAC Firewall Policy ID'
access_token = '***'

url = f"https://api.extremecloudiq.com/user-profiles/{user_profile_id}/mac-filrewall-policies/:detach"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "policy_id": mac_firewall_policy_id,
  "traffic": "INBOUND"
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
