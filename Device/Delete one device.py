import requests

url = "https://api.extremecloudiq.com/devices/***"

payload={}
headers = {
  'accept': '*/*',
  'Authorization': '***'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
