import requests

url = "https://api.extremecloudiq.com/locations/floorplan"

payload={}
files=[
  ('file',('file',open('/path/to/file','rb'),'application/octet-stream'))
]
headers = {
  'accept': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
