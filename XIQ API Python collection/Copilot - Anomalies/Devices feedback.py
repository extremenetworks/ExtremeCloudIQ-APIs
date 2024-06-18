import requests
import json

access_token = '***'

url = "https://api.extremecloudiq.com/copilot/anomalies/devices/feedback"

payload = json.dumps({
  "anomaly_type": "POE_FLAPPING",
  "anomaly_id": "string",
  "feedback_type": "LIKE",
  "feedback": "string"
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
