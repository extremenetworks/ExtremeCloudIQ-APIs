import requests
import json

ssid_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/ssids/{ssid_id}/mode/ppsk"

payload = json.dumps({
  "key_management": "WPA_PSK",
  "encryption_method": "CCMP",
  "user_group_ids": [
    0 # The user group IDs to be attached to the SSID, cannot be empty
  ],
  "enable_max_clients_per_ppsk": True,
  "max_clients_per_ppsk": 0,
  "enable_mac_bind": True,
  "max_macs_per_ppsk": 0,
  "ppsk_server_id": 0 # The PPSK server device ID
})
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
