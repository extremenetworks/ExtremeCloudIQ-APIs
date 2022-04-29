import requests

access_token = '***'

url = "https://api.extremecloudiq.com/auth/permissions/:check"

payload="{\n  \"uri\": \"https://api.extremecloudiq.com/auth/apitoken/info\",\n  \"method\": \"get\"\n}"
headers = {
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text) 
