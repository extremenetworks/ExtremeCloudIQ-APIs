import requests
import json

device_id = 0
client_monitor_profile_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/devices/{device_id}/client-monitor"

payload = json.dumps({
  "client_monitor_profile_id": client_monitor_profile_id,
  "enable": True
})
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
