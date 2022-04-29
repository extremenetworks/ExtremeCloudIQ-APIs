import requests

access_token = '***'

url = "https://api.extremecloudiq.com/hiq/context/creating"

payload="1"
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
