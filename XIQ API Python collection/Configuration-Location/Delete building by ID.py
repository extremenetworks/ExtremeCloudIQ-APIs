import requests

url = "https://api.extremecloudiq.com/locations/building/{{building_id}}"

payload = ""
headers = {
  'accept': 'application/json'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
