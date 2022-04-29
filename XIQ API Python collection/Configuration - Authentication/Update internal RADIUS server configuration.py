import requests
import json

int_radius_id = 0
access_token = '***'

url =f"https://api.extremecloudiq.com/radius-servers/external/{int_radius_id}"

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
})
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
