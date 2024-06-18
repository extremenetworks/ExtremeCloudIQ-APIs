import requests

device_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/devices/{device_id}/monitor/ipv4-routing?page=1&limit=10"

payload = {}
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
