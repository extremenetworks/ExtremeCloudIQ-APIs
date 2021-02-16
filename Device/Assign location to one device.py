import requests

url = "https://api.extremecloudiq.com/devices/***/location"

payload="{\n    \"location_id\":***,\n    \"x\":***,\n    \"y\":***,\n    \"latitude\":null,\n    \"longitude\":null\n    \n}"
headers = {
  'accept': '*/*',
  'Content-Type': 'application/json',
  'Authorization': '***'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
