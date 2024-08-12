import requests

owner_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/afcserver?ownerId={owner_id}"

payload = {}
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
