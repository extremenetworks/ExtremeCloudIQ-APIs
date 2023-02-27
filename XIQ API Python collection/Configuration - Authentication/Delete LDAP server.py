import requests

ldap_id = 0 # The LDAP server ID
access_token = '***'

url =f"https://api.extremecloudiq.com/ldap-servers/{ldap_id}"

payload={}
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
