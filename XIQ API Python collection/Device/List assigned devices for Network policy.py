import requests

np_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/devices/network-policy/{np_id}?page=1&limit=10"

payload={}
headers = {
  'accept': '***',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
