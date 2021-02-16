import requests

url = "https://api.extremecloudiq.com/ssids?page=1&limit=80"

payload={}
headers = {
  'accept': 'application/json',
  'Authorization': '***'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
