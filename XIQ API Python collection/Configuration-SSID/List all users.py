import requests

url = "https://api.extremecloudiq.com/ssids/users"

payload = ""
headers = {
  'accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
