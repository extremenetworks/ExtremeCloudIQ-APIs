import requests

url = "https://api.extremecloudiq.com/devices/***/"

payload={}
headers = {
  'accept': '*/*',
  'Authorization': '***'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
