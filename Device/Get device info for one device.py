import requests

url = "https://api.extremecloudiq.com/devices/***"

payload={}
headers = {
  'accept': 'application/json',
  'Authorization': 'B***'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
