import requests

device_id = 0
access_token = '***'
description = "string"

url = f"https://api.extremecloudiq.com/devices/{device_id}/description"

payload = description
headers = {
  'accept': '*/*',
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'text/plain'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
