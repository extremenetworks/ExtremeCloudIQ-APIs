import requests

vp_id = 0 # VLAN Profile ID
access_token = '***'

url = f"https://api.extremecloudiq.com/vlan-profiles/{vp_id}"

payload={}
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.headers) # LRO location URL is included in headers
print(response.text)
