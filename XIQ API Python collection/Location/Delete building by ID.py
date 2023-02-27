import requests

building_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/locations/building/{building_id}?force_delete=false"

payload = {}
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
