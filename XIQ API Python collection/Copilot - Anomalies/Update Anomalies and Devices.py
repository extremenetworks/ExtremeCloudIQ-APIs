import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/copilot/anomalies/update-device-action"

payload = json.dumps({
  "anomalyDetails": [
    {
      "buildingId": 0,
      "locationId": 0,
      "anomalyId": "string",
      "anomalyType": "POE_STABILITY"
    }
  ],
  "actionType": "MUTE"
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
