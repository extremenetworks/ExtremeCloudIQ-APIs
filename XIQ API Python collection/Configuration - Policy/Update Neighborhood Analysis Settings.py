import requests
import json

neigh_analysis_id = 0 # The neighborhood analysis settings ID
access_token = '***'

url = f"https://api.extremecloudiq.com/radio-profiles/neighborhood-analysis/{neigh_analysis_id}"

payload = json.dumps({
  "enable_background_scan": True,
  "background_scan_interval": 1440,
  "enable_skip_scan_when_clients_connected": True,
  "enable_skip_scan_when_clients_in_power_save_mode": True,
  "enable_skip_scan_when_process_voice_traffic": True
})
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
