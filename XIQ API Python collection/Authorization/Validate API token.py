import requests

access_token = "****"

url = "https://api.extremecloudiq.com/auth/apitoken/:validate"

payload = access_token
headers = {
  'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)