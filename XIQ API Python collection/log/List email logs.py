import requests

url = "https://api.extremecloudiq.com/logs/email?page=1&limit=10&username=&startTime=&endTime="

payload={}
headers = {
  'accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
