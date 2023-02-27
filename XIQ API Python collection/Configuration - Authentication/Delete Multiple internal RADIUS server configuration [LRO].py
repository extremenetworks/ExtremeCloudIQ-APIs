import requests

int_radius_id = 0 # The internal RADIUS server ID
access_token = '***'

url =f"https://api.extremecloudiq.com/radius-servers/internal?ids={int_radius_id}&async=false"

payload={}
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.headers) # LRO location URL is included in headers
print(response.text)

print(f"Long Running Status URL - {response.headers['Location']}")