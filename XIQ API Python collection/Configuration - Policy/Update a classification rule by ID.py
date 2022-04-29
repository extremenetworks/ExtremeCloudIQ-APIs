import requests
import json

class_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/classification-rules/{class_id}"

payload = json.dumps({
  "name": "string",
  "description": "string",
  "classifications": [
    {
      "classification_type": "CLASSIFICATION_TYPE_UNSPECIFIED",
      "match": True,
      "classification_type_id": 0
    }
  ]
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
