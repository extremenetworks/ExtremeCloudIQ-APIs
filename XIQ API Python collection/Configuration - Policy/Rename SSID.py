import requests
import json

ssid_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/ssids/{ssid_id}/:rename"

payload = "string"
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
