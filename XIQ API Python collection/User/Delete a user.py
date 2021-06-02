import requests

url = "https://api.extremecloudiq.com/users/admin User ID"

payload = ""
headers = {
  'Authorization': ''
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
