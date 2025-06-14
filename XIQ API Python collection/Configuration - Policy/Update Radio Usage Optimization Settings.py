import requests
         
baseUrl = 'api.extremecloudiq.com'
radio_usage_opt_id = 'Radio Usage Optimization Setting ID'
access_token = '***'

url = f"https://{baseUrl}/radio-profiles/radio-usage-opt/{radio_usage_opt_id}"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
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
}



response = requests.put(url, headers=headers, params=params)

print("Status Code:", response.status_code)

content_type = response.headers.get('Content-Type')
if content_type and 'application/json' in content_type:
    try:
        print("Response Body:", response.json())
    except ValueError:
        print("Response is not valid JSON")
else:
    print("Content-Type is not application/json")
    print(response.text)
