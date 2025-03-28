import requests
         

access_token = '***'

url = f"https://api.extremecloudiq.com/locations/import/ekahau"
headers = {'Authorization': f'Bearer {access_token}'}
params = {'floorAssociations': '[{"floorName":"1st floor","parentBuildingId":1}]', 'outdoorSiteAssociations': '[{"floorName":"2nd floor","parentSiteGroupId":2,"countryCode":124}]'}

# async: false (disabled)
# importCustomApConfigurations: true (disabled)

from requests_toolbelt.multipart.encoder import MultipartEncoder

files = {"file": ('filename', open('Path-to-file/file.ext', 'rb'),'image/jpeg')}
payload = MultipartEncoder(fields=files)
headers["Content-Type"] = payload.content_type
response = requests.post(url, headers=headers, params=params, data=payload)

print("Status Code:", response.status_code)

content_type = response.headers.get('Content-Type')
lro_url = response.headers.get('Location')
if lro_url:
    print(lro_url)
elif content_type and 'application/json' in content_type:
    try:
        print("Response Body:", response.json())
    except ValueError:
        print("Response is not valid JSON")
else:
    print("Content-Type is not application/json")
    print(response.text)
