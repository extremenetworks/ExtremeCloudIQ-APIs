import requests

device_id = 0
imageName = 'image name'
access_token = '***'

url = f"https://api.extremecloudiq.com/devices/{device_id}/gallery-image?{imageName}"

payload = {}
headers = {
  'accept': '*/*',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
