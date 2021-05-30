import requests

url = "https://api.extremecloudiq.com/ssids/***/"

payload="string"
headers = {
  'accept': '*/*',
  'Content-Type': 'application/json',
  'Authorization': '***'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
