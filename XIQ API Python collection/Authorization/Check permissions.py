import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/auth/permissions/:check"

payload = json.dumps({
  "uri": "https://api.extremecloudiq.com/auth/apitoken/info",
  "method": "get"
})
headers = {
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text) 
