import requests

access_token = '***'

url = "https://api.extremecloudiq.com/users/external?page=1&limit=10"

payload = ""
headers = {
    'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
