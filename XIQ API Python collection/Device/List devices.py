import requests

page = 1
limit = 10
access_token = '***'

url = f"https://api.extremecloudiq.com/devices?page={page}&limit={limit}&views=FULL&async=false"

payload={}
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.headers) # LRO location URL is included in headers
print(response.text)
