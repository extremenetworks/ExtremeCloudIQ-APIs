import requests

url = "https://api.extremecloudiq.com/devices/location/"

payload="{\"ids\":[***]}"
headers = {
  'accept': '*/*',
  'Content-Type': 'application/json',
  'Authorization': '***'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
