import requests
import json

access_token = '***'

url ="https://api.extremecloudiq.com/radius-servers/internal"

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
        "default_server_id": 0, # The default external user directory server id, could be active directory server id(get the id list from endpoint: '/ad-servers') or LDAP server id(get the id list from endpoint: '/ldap-servers') depends on the 'external_user_directory_type'
        "server_role": "PRIMARY"
      }
    ]
  },
  "ca_certificate_id": 0, # The CA certificate ID, which could be fetched from endpoint: '/certificates' and pick up with type 'CA'
  "server_certificate_id": 0, # The Server certificate ID, which could be fetched from endpoint: '/certificates' and pick up with type 'CERT'
  "server_key_id": 0, # The Server key ID, which could be fetched from endpoint: '/certificates' and pick up with type 'KEY'
  "device_ids": [
    0 # The list of device ID associated with the internal RADIUS server
  ],
  "clients": [
    {
      "id": 0, # The RADIUS client ID
      "shared_secret": "string",
      "description": "string",
      "l3_address_profile_id": 0 # The associate L3 address profile ID
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
