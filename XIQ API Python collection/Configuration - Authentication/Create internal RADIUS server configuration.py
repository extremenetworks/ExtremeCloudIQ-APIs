import requests
import json

access_token = '***'

url ="https://api.extremecloudiq.com/radius-servers/external"

payload = json.dumps({
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
  "authentication_server_port": 0,
  "active_session_limit": 0,
  "active_session_age_timeout": 0,
  "external_user_directory": {
    "ldap_retry_interval": 0,
    "local_check_interval": 0,
    "remote_check_interval": 0,
    "enable_radius_server_credential_caching": True,
    "cache_lifetime": 0,
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
})
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
