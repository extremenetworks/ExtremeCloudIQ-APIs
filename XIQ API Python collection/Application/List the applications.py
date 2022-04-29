import requests

access_token = '***'

url = "https://api.extremecloudiq.com/applications?page=1&limit=10&predefined=true"

payload = ""
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
