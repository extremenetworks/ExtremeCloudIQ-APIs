import requests

owner_id = 0
serial_number = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/ap/afc/diagnostics/{serial_number}?ownerId={owner_id}"

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers)

print(response.text)
