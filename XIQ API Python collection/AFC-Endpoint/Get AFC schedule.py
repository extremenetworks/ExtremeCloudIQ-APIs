import requests

owner_id = 0
folder_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/site/afc/schedule?ownerId={owner_id}&folderId={folder_id}"

payload = {}
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
