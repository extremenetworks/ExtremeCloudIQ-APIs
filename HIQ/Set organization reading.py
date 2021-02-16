import requests

url = "https://api.extremecloudiq.com/hiq/context/reading"

payload="[\n  ***\n]"
headers = {
  'Authorization': '***',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
