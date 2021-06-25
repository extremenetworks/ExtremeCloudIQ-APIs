import requests

url = "https://api.extremecloudiq.com/pcg/key-based/***/keys/?userIds=***"

payload={}
headers = {
  'accept': '*/*',
  'Authorization': '***'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
