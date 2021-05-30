import requests

url = "https://api.extremecloudiq.com/user/profile"

payload={}
headers = {
  'Authorization': '***'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
