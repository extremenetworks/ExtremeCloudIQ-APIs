import requests
import json

url = "https://api.extremecloudiq.com/ccgs"

payload = json.dumps({
  "name": "NameOfCGG",
  "description": "Add New CCG",
  "device_ids": [
    44238164,
    45054207
  ]
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
