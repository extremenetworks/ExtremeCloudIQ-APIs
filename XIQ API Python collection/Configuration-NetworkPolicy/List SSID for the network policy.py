import requests

url = "https://api.extremecloudiq.com/network-policies/***/ssids?page=1&limit=50"

payload={}
headers = {
  'accept': 'application/json',
  'Authorization': '***'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
