import requests

location_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/locations/tree/maps?page=1&limit=10&locationId={location_id}&expandChildren=true"

payload = {}
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
