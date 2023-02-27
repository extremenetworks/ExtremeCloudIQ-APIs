import requests

np_id = 0 # Network Policy ID
access_token = '***'

url = f"https://api.extremecloudiq.com/network-policies/{np_id}/ssids?page=1&limit=50"

payload={}
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
