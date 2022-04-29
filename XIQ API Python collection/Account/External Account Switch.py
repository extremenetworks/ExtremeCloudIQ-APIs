import requests

access_token = '***'

url = "https://api.extremecloudiq.com/account/:switch?id=101000"

payload = ""
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
