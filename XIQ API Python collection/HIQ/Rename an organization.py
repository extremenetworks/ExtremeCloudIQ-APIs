import requests

url = "https://api.extremecloudiq.com/hiq/organizations/***/"

payload="[***]"
headers = {
  'Authorization': '***',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
