import requests

deployment_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/deployments/{deployment_id}"


headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers)

print(response.text)
