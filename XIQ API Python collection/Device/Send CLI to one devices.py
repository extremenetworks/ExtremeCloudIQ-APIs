import requests
import json

device_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/devices/{device_id}/:cli"

payload = json.dumps([
  "CLI commands as string"
])
headers = {
  'accept': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
