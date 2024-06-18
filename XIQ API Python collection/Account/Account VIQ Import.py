import requests

access_token = '***'

url = "https://api.extremecloudiq.com/account/viq/import?timeoutInSeconds=1800&excludeDeviceFirmware=false"

payload = {}
files=[
  ('file',('file',open('/path/to/file','rb'),'application/octet-stream'))
]
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
