import requests

access_token = '***'

operation_id = '*****'

url = f"https://api.extremecloudiq.com/operations/{operation_id}"

payload={}
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
