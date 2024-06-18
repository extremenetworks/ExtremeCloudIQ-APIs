import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/copilot/anomalies/devices/update-action"

payload = json.dumps({
  "anomaly_type": "POE_STABILITY",
  "action_type": "MUTE",
  "location_id": 0,
  "anomaly_id": "string"
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
