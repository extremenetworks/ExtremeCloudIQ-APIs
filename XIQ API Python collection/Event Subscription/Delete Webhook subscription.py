import requests

url = "https://api.extremecloudiq.com/subscriptions/webhook/{{web_id}}"

payload={}
headers = {
  'accept': 'application/json'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
