import requests

url = "https://api.extremecloudiq.com/auth/apitoken"

payload="{\n  \"description\": \"Token for read account only\",\n  \"expire_time\": 1625185800,\n  \"permissions\": [\n    \"account:r\"\n  ]\n}"
headers = {
  'Authorization': '***',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
