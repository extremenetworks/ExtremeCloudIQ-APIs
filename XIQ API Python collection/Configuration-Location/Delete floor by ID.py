import requests
import json

url = "https://api.extremecloudiq.com/locations/floor/{{floor_id}}"

payload = "\n}"
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
