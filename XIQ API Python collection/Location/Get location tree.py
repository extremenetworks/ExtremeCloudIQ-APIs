import requests

parent_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/locations/tree?parentId={parent_id}&expandChildren=true"
 
payload={}
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
