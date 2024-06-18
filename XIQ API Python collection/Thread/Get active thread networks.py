import requests

folderId = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/thread/networks?page=1&limit=10&folderId]{folderId}"

payload = {}
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
