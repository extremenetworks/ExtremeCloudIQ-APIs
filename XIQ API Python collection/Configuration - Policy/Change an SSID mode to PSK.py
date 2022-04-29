import requests
import json

ssid_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/ssids/{ssid_id}/mode/psk"

payload = json.dumps({
  "key_management": "WPA_PSK",
  "encryption_method": "CCMP",
  "anti_logging_threshold": 0,
  "key_type": "ASCII",
  "key_value": "string",
  "sae_group": "ALL",
  "transition_mode": True
})
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
