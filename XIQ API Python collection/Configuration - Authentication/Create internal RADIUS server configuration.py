import requests
         
baseUrl = 'api.extremecloudiq.com'
access_token = '***'

url = f"https://{baseUrl}/radius-servers/internal"
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
  "active_session_age_timeout": 1800,
  "external_user_directory": {
    "ldap_retry_interval": 600,
    "local_check_interval": 300,
    "remote_check_interval": 30,
    "enable_radius_server_credential_caching": True,
    "cache_lifetime": 86400,
    "user_group_attribute": "memberOf",
    "external_user_directory_type": "OPEN_LDAP",
    "entries": [
      {
        "default_server_id": 0,
        "server_role": "PRIMARY"
      }
    ]
  },
  "ca_certificate_id": 0,
  "server_certificate_id": 0,
  "server_key_id": 0,
  "device_ids": [
    0
  ],
  "clients": [
    {
      "id": 0,
      "shared_secret": "string",
      "description": "string",
      "l3_address_profile_id": 0
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
