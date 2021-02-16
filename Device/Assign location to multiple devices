import requests

url = "https://api.extremecloudiq.com/devices/location/"

payload="{\"devices\":{\"ids\":[***]},\"device_location\":{\"location_id\":***,\"x\":0,\"y\":0,\"latitude\":0,\"longitude\":0}}"
headers = {
  'accept': '*/*',
  'Content-Type': 'application/json',
  'Authorization': '***'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
