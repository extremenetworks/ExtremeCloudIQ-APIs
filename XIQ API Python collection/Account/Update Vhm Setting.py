import requests
         
vhm_id = 'Vhm ID'
access_token = '***'

url = f"https://api.extremecloudiq.com/account/vhm/setting/{vhm_id}"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "enable_copilot": True,
  "enable_ssh": True,
  "enable_supplemental_cli": True,
  "enable_wireless_onboarding": True,
  "enable_password_for_exos_voss": True
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
