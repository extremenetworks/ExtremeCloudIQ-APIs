import requests

access_token = '***'

url = "https://api.extremecloudiq.com/l3-address-profiles"

payload={}
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
