import requests
import json

radio_usage_opt_id = 0 # The radio usage optimization settings ID
access_token = '***'

url = f"https://api.extremecloudiq.com/radio-profiles/radio-usage-opt/radio_usage_opt_id"

payload = json.dumps({
  "preamble": "string",
  "beacon_period": 3500,
  "enable_frame_burst": True,
  "enable_smart_antenna": True,
  "enable_backhaul_failover": True,
  "wireless_backhaul_switch_trigger_time": 5,
  "wired_backhaul_revert_hold_time": 300,
  "enable_band_steering": True,
  "band_steering_mode": "string",
  "ratio_for5g_clients": 100,
  "ignore_initial_client_connection_number": 100,
  "enable_client_load_balancing": True,
  "load_balancing_mode": "string",
  "crc_error_rate_per_device": 99,
  "rf_interference_per_device": 99,
  "average_airtime_per_client": 5,
  "anchor_period": 600,
  "neighbor_query_interval": 600,
  "enable_weak_signal_probe_request_suppression": True,
  "weak_snr_threshold": 100,
  "enable_safety_net": True,
  "safety_net_period": 300,
  "enable_high_density": True,
  "management_frame_basic_data_rate": "string",
  "enable_suppress_successive_probe_request": True,
  "probe_response_reduction_option": "string",
  "suppression_limit": 10,
  "enable_radio_balance": True,
  "mac_oui_ids": [
    0
  ],
  "enable_ampdu": True,
  "enable_mu_mimo": True,
  "enable_ofdma_down_link": True,
  "enable_ofdma_up_link": True,
  "bss_coloring": 63,
  "enable_target_weak_time": True
})
headers = {
  'accept': 'application/json',
  'Authorization': 'Bearer ' + access_token,
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
