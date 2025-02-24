import requests
         
int_radius_id = 'The ID for internal RADIUS server'
access_token = '***'

url = f"https://api.extremecloudiq.com/radius-servers/internal/{int_radius_id}"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "name": "string",
  "description": "string",
  "authentication_method_group": "TLS_PEAP_TTLS_LEAP_MD5",
  "default_authentication_method": "TLS",
  "enable_verify_server_cert": True,
  "server_key_password": "string",
  "enable_check_cert_common_name": True,
  "enable_check_user_for_tls_auth": True,
  "enable_check_user_for_peap_auth": True,
  "enable_check_user_for_ttls_auth": True,
  "enable_authentication_server": True,
  "enable_radius_accounting_settings": True,
  "authentication_server_port": 1812,
  "active_session_limit": 0,
  "active_session_age_timeout": 30,
  "ca_certificate_id": 0,
  "server_certificate_id": 0,
  "server_key_id": 0,
  "clients": [
    {
      "id": 0,
      "shared_secret": "string",
      "description": "string",
      "l3_address_profile_id": 0
    }
  ]
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
