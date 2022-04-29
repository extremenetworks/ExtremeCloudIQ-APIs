import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/devices/"

payload = json.dumps({
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
)
headers = {
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
