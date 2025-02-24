import requests
         

access_token = '***'

url = f"https://api.extremecloudiq.com/ldap-servers"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "name": "string",
  "description": "string",
  "enable_tls": True,
  "bind_dn": "string",
  "bind_dn_password": "string",
  "base_dn": "string",
  "l3_address_profile_id": 0,
  "protocol_type": "LDAP",
  "enable_strip_realm_name": False,
  "destination_port": 10,
  "verification_mode": "TRY",
  "ca_certificate_id": 0,
  "client_certificate_id": 0,
  "client_key_id": 0,
  "client_key_password": "string"
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
