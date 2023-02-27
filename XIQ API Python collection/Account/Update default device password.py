import requests

access_token = '***'

password = '****'

url = "https://api.extremecloudiq.com/account/viq/default-device-password"

payload = password
headers = {
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'text/plain'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response)
