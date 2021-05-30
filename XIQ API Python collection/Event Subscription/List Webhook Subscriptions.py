import requests

url = "https://api.extremecloudiq.com/subscriptions/webhook"

payload={}
headers = {
  'accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
