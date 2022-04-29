import requests

filename = 'filename in XIQ'
filepathname = 'path with filename to upload'

access_token = '***'

url = "https://api.extremecloudiq.com/locations/floorplan"

payload={}
files={
            'file' : (f'{filename}', open(filepathname, 'rb'), 'image/png'),
            'type': 'image/png'
        }
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
