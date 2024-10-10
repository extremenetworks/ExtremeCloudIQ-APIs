import requests

floor_associations = [] # Describes how Ekahau floors are imported into XIQ as floors in buildings. ex. [{"floorName":"1st floor","parentBuildingId":1}]
outdoor_site_associations = [] # Describes how Ekahau floors are Imported into XIQ as outdoor sites in site groups. ex. [{"floorName":"2nd floor","parentSiteGroupId":2,"countryCode":124}]

access_token = '***'
path_to_file = '/path-to-file/filename'

url = f"https://api.extremecloudiq.com/locations/import/ekahau?async=false&floorAssociations={floor_associations}&outdoorSiteAssociations={outdoor_site_associations}&importCustomApConfigurations=true"

payload = {}
files=[
  ('file',('file',open(path_to_file,'rb'),'application/octet-stream'))
]
headers = {
  'Content-Type': 'multipart/form-data\'',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
