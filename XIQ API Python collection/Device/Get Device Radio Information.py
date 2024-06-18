import requests

device_id = 0 
access_token = '***'

url = f"https://api.extremecloudiq.com/devices/radio-information?page=1&limit=10&deviceIds={device_id}"

payload = {}
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
