import requests

l3_address_profile = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/l3-address-profiles/{l3_address_profile}"

payload = {}
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
