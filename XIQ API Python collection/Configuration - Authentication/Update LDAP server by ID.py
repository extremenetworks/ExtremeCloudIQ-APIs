import requests
import json

ldap_id = 0
access_token = '***'

url =f"https://api.extremecloudiq.com/ldap-servers/{ldap_id}"

payload = json.dumps({
  "name": "test-ldap-server-1",
  "description": "test ldap server 1",
  "enable_tls": True,
  "bind_dn": "extremenetworks.com",
  "bind_dn_password": "888888",
  "base_dn": "extremenetworks.com",
  "l3_address_profile_id": 1,
  "protocol_type": "LDAPS",
  "enable_strip_realm_name": False,
  "destination_port": 20,
  "verification_mode": "DEMAND",
  "ca_certificate_id": 100,
  "client_certificate_id": 200,
  "client_key_id": 300,
  "client_key_password": "123456"
})
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
