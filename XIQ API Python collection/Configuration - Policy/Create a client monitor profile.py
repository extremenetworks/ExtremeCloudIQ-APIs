import requests
import json

url = "https://api.extremecloudiq.com/client-monitor-profiles"

payload = json.dumps({
  "name": "string",
  "description": "string",
  "association": {
    "trigger_times": 10,
    "report_interval": 3600
  },
  "authentication": {
    "trigger_times": 10,
    "report_interval": 3600
  },
  "networking": {
    "trigger_times": 10,
    "report_interval": 3600
  }
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
