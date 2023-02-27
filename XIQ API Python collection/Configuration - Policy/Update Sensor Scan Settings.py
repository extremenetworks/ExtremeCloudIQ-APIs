import requests
import json

sensor_scan_id = 0 # The sensor scan settings ID
access_token = '***'

url = f"https://api.extremecloudiq.com/radio-profiles/sensor-scan/{sensor_scan_id}"

payload = json.dumps({
  "enable_scan_all_channels": True,
  "dwell_time": "string",
  "scan_channels": "string"
})
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
