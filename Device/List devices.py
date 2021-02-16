import requests

url = "https://api.extremecloudiq.com/devices?page=1&limit=50"

payload={}
headers = {
  'Authorization': '***'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
