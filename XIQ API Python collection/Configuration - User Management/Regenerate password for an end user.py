import requests

user_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/endusers/{user_id}/:regenerate-password"

payload={}
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
