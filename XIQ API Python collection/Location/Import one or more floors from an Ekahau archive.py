import requests

access_token = '***'
path_to_file = '/path-to-file/filename'

url = "https://api.extremecloudiq.com/locations/import/ekahau"

payload = {'associations': '{"1st floor":1}'}
files=[
  ('file',('file',open(path_to_file,'rb'),'application/octet-stream'))
]
headers = {
  'Content-Type': 'multipart/form-data\'',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
