import requests

access_token = '***'

url = "https://api.extremecloudiq.com/devices?page=1&limit=50&views=FULL"

payload={}
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
