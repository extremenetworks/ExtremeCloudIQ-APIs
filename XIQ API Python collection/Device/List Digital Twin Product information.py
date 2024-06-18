import requests

url = "https://api.extremecloudiq.com/devices/digital-twin?page=1&limit=10"

payload = {}
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
