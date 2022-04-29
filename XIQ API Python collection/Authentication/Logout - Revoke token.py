import requests

access_token = '***'

url = "https://api.extremecloudiq.com/logout"

payload={}
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)