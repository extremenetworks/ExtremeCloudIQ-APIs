import requests

url = "https://api.extremecloudiq.com/devices/network-policy/***?page=1&limit=10"

payload={}
headers = {
  'accept': '***'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
