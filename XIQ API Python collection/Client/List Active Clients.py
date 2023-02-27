import requests

access_token = '***'

url = "https://api.extremecloudiq.com/clients/active?page=1&limit=10&views=FULL"

payload={}
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
