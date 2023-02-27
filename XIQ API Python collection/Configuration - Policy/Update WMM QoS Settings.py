import requests
import json

radio_qos_id = 0 # The radio QoS settings ID
access_token = '***'

url = f"https://api.extremecloudiq.com/radio-profiles/wmm-qos/{radio_qos_id}"

payload = json.dumps({
  "arbitration_interframe_space": 15,
  "min_contention_window": 15,
  "max_contention_window": 15,
  "transmission_opportunity_limit": 8192,
  "enable_no_ack": True
})
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
