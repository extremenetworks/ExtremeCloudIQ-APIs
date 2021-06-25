import requests

url = "https://api.extremecloudiq.com/clients/summary"

payload = ""
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
