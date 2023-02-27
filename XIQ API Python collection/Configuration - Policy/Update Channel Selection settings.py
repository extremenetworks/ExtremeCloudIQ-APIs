import requests
import json

channel_selection_id = 0
access_token = '***'

url = f"https://api.extremecloudiq.com/radio-profiles/channel-selection/{channel_selection_id}"

payload = json.dumps({
  "enable_dynamic_channel_switching": True,
  "channel_width": "string",
  "enable_dynamic_frequency_selection": True,
  "enable_static_channel": True,
  "enable_zero_wait_dfs": True,
  "enable_use_last_selection": True,
  "exclude_channels": "string",
  "exclude_channels_width": "string",
  "channel": 165,
  "enable_limit_channel_selection": True,
  "channel_region": "string",
  "channel_model": 4,
  "channels": "string",
  "enable_channel_auto_selection": True,
  "channel_selection_start_time": "string",
  "channel_selection_end_time": "string",
  "enable_avoid_switch_channel_if_clients_connected": True,
  "channel_selection_max_clients": 100,
  "enable_switch_channel_if_exceed_threshold": True,
  "rf_interference_threshold": 80,
  "crc_error_threshold": 80
})
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
