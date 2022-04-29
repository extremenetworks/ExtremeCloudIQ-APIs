import requests
import json

device_id = 0 
access_token = '***'

url = f"https://api.extremecloudiq.com/devices/radius=proxy/:revoke?ids={device_id}"

payload={}
headers = {
  'accept': '*/*',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
