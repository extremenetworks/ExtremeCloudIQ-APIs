import requests

url = "https://api.extremecloudiq.com/devices/:cli"

payload="{\n  \"devices\": {\n    \"ids\": [\n      ***\n    ]\n  },\n  \"clis\": [\n    \"***\"\n  ]\n}"
headers = {
  'Authorization': '***',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
