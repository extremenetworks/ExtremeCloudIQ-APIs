import requests

org_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/hiq/organizations/{org_id}"

payload={}
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
