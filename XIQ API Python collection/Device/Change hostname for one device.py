import requests

device_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/devices/{device_id}/hostname?hostname=test"

payload={}
headers = {
  'accept': '*/*',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
