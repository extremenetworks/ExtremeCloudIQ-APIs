import requests
import json

serial_number = 0 
access_token = '***'

url = "https://api.extremecloudiq.com/devices/:check-ownership"

payload = json.dumps(f"{serial_number}")
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
