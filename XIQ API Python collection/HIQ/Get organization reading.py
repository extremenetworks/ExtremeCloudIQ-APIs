import requests

access_token = '***'

url = "https://api.extremecloudiq.com/hiq/context/reading"

payload={}
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
