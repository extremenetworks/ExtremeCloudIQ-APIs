import requests

int_radius_id = 0 # The internal RADIUS server ID
access_token = '***'

url =f"https://api.extremecloudiq.com/radius-servers/internal/{int_radius_id}"

payload={}
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
