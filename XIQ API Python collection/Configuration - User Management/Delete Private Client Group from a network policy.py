import requests
import json

np_id = 0 # Network Policy ID
pcgk_id = 0 # ID of the Key-based PCG entity
access_token = '***'

url = f"https://api.extremecloudiq.com/pcgs/key-based/network-policy-{np_id}?ids={pcgk_id}"

payload={}
headers = {
  'accept': '*/*',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
