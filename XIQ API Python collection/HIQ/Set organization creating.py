import requests

url = "https://api.extremecloudiq.com/hiq/context/creating"

payload="1"
headers = {
  'Authorization': '***',
  'Content-Type': 'text/plain'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
