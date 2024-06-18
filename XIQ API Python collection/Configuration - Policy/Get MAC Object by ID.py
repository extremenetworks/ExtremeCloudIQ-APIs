import requests

mac_object_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/mac-object-profiles/{mac_object_id}"

payload = {}
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
