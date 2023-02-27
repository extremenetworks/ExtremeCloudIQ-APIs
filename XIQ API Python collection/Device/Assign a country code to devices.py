import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/devices/country-code/:assign"


payload = json.dumps({
  "devices": {
    "ids": [
        0
    ],
    "country_code": "AFGHANISTAN_4"
  }
})
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
