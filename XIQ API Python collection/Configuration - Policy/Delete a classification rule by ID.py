import requests

class_id = 0 # Classification Rule ID
access_token = '***'

url = f"https://api.extremecloudiq.com/classification-rules/{class_id}"

payload={}
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
