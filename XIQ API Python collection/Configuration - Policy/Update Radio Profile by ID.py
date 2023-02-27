import requests
import json

radio_profile_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/radio-profiles/{radio_profile_id}"

payload = json.dumps({
  "name": "string",
  "description": "string",
  "transmission_power": 20,
  "max_transmit_power": 20,
  "transmission_power_floor": 20,
  "transmission_power_max_drop": 18,
  "max_clients": 255,
  "enable_client_transmission_power": True,
  "client_transmission_power": 20,
  "radio_mode": "B_G",
  "enable_ofdma": True
})
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
