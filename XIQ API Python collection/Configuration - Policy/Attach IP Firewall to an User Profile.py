import requests
         
user_profile_id = 'User Profile ID'
ip_firewall_policy_id = 'IP Firewall Policy ID'
access_token = '***'

url = f"https://api.extremecloudiq.com/user-profiles/{user_profile_id}/ip-filrewall-policies/:attach"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "policy_id": ip_firewall_policy_id,
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
