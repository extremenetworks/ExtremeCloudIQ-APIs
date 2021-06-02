import requests

url = "https://api.extremecloudiq.com/devices/config/deploy/overview"

payload={}
headers = {
  'accept': 'application/json',
  'Authorization': '***'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
