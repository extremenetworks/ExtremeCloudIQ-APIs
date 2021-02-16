import requests

url = "https://api.extremecloudiq.com/network-policies?page=1&limit=10"
 
payload={}
headers = {
  'accept': 'application/json',
  'Authorization': '***'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
