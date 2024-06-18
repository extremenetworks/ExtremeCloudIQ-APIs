import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/copilot/anomalies/update-action"

payload = json.dumps({
  "anomaly_type": "POE_FLAPPING",
  "action_type": "MUTE",
  "building_id": 0
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
