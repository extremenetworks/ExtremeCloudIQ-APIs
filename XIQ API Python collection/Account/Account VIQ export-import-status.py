import requests

viqOperationType='EXPORT' # Available values : EXPORT, IMPORT
access_token = '***'

url = f"https://api.extremecloudiq.com/account/viq/export-import-status?viqOperationType={viqOperationType}"

payload = {}
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
