import requests

url = "https://api.extremecloudiq.com/login"

payload="{\n  \"username\": \"***\",\n  \"password\": \"*** s\"\n}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
