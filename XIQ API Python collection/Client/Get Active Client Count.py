import requests

access_token = '***'

url = "https://api.extremecloudiq.com/clients/active/count"

payload={}
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
