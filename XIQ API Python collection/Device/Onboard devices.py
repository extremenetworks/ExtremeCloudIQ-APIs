import requests
         
baseUrl = 'https://api.extremecloudiq.com'
access_token = '***'

url = f"{baseUrl}/devices/:onboard"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "extreme": {
    "sns": [
      "string"
    ]
  },
  "exos": {
    "sns": [
      "string"
    ]
  },
  "voss": {
    "sns": [
      "string"
    ]
  },
  "wing": {
    "sn_to_mac": {
      "additionalProp1": "string",
      "additionalProp2": "string",
      "additionalProp3": "string"
    }
  },
  "dell": {
    "sn_to_st": {
      "additionalProp1": "string",
      "additionalProp2": "string",
      "additionalProp3": "string"
    }
  }
}


response = requests.post(url, headers=headers, params=params)

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
