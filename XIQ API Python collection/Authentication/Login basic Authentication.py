import requests
import json

username = '***'
password = '***'

url = "https://api.extremecloudiq.com/login"


payload = json.dumps({
  'username': username,
  'password': password
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
 
