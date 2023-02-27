import requests

ex_radius_id = 0 # The ID for external RADIUS server
access_token = '***'

url =f"https://api.extremecloudiq.com/radius-servers/external/{ex_radius_id}"

payload={}
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
