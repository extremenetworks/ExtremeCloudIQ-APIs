import requests

url = "https://api.extremecloudiq.com/devices/***/hostname?hostname=test"

payload={}
headers = {
  'accept': '*/*',
  'Authorization': '***'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
