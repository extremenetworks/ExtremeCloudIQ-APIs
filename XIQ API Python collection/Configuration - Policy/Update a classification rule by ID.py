import requests
         
baseUrl = 'api.extremecloudiq.com'
class_id = 'Classification Rule ID'
access_token = '***'

url = f"https://{baseUrl}/classification-rules/{class_id}"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "name": "string",
  "description": "string",
  "classifications": [
    {
      "classification_type": "CLASSIFICATION_TYPE_UNSPECIFIED",
      "match": True,
      "classification_type_id": 0
    }
  ]
}


response = requests.put(url, headers=headers, params=params)

print("Status Code:", response.status_code)

content_type = response.headers.get('Content-Type')
if content_type and 'application/json' in content_type:
    try:
        print("Response Body:", response.json())
    except ValueError:
        print("Response is not valid JSON")
else:
    print("Content-Type is not application/json")
    print(response.text)
