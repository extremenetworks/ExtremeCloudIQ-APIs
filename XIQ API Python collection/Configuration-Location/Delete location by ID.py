import requests

url = "https://api.extremecloudiq.com/locations/{{loc_id}}"

payload = ""
headers = {
  'accept': 'application/json'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
