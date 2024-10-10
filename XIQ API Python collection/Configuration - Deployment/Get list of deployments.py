import requests

page = 1
limit = 10
access_token = '***'

url = f"https://api.extremecloudiq.com/deployments?page={page}&limit={limit}"

headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers)

print(response.text)
