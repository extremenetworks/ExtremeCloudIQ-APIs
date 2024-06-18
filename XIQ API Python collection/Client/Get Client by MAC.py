import requests

client_mac = '**'
access_token = '***'

url = f"https://api.extremecloudiq.com/clients/byMac/{client_mac}?views=FULL"

payload = {}
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
