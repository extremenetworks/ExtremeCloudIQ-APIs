import requests

client_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/{client_id}?views=FULL"

payload={}
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
