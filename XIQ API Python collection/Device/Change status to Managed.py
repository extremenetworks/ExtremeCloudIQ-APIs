import requests

url = "https://api.extremecloudiq.com/devices/"

payload="{\n  \"ids\": [\n    0\n  ]\n}"
headers = {
  'Authorization': '***',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
