import requests
import json

device_id = 0
radiusProxy_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/devices/radius=proxy/:assign?ids={device_id}&radiusProxyId={radiusProxy_id}"

payload={}
headers = {
  'accept': '*/*',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
