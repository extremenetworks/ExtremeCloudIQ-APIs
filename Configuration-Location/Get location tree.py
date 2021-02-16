import requests

url = "https://api.extremecloudiq.com/locations/tree?parentId=***&expandChildren=true"

payload={}
headers = {
  'accept': 'application/json',
  'Authorization': '***'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
