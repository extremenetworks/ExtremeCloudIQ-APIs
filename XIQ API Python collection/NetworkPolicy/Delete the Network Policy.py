import requests

np_id = 0 # Network Policy ID
access_token = '***'

url = f"https://api.extremecloudiq.com/network-policies/{np_id}"

payload={}
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
