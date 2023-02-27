import requests
import json

floor_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/locations/floor/{floor_id}?force_delete=false"

payload = {}
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
