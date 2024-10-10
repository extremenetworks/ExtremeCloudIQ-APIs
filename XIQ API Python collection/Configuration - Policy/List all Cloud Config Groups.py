import requests

access_token = '***'

page = 1
limit = 10
url = f"https://api.extremecloudiq.com/ccgs?page={page}&limit={limit}"

payload={}
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
