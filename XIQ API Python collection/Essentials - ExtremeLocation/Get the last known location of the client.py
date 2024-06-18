import requests

client_mac = ''
access_token = '***'

url = f"https://api.extremecloudiq.com/essentials/eloc/clients/{client_mac}/last-known-location?floorId=Floor ID &parentId=Building ID"

payload = {}
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
