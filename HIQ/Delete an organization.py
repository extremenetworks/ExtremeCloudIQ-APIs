import requests

url = "https://api.extremecloudiq.com/hiq/organizations/***"

payload={}
headers = {
  'Authorization': '***'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
