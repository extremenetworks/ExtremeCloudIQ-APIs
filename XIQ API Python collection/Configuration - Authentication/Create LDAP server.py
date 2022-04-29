import requests
import json

access_token = '***'

url ="https://api.extremecloudiq.com/ldap-servers"

payload = json.dumps({
  "name": "test-ldap-server",
  "description": "test ldap server",
  "enable_tls": True,
  "bind_dn": "extreme.com",
  "bind_dn_password": "123456",
  "base_dn": "extreme.com",
  "l3_address_profile_id": 10,
  "protocol_type": "LDAP",
  "enable_strip_realm_name": False,
  "destination_port": 10,
  "verification_mode": "TRY",
  "ca_certificate_id": 1000,
  "client_certificate_id": 2000,
  "client_key_id": 30000,
  "client_key_password": ""
})
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
