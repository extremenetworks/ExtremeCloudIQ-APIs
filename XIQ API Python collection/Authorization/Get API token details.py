import requests

url = "https://api.extremecloudiq.com/auth/apitoken/info"

payload={}
headers = {
  'Authorization': 'xyz'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
