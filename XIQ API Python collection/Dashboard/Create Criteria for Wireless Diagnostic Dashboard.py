import requests
         
baseUrl = 'api.extremecloudiq.com'
access_token = '***'

url = f"https://{baseUrl}/dashboard/wireless/dashboard/criteria"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "device_health_criteria": {
    "cpu_utilization": 0,
    "memory_utilization": 0,
    "poe": 0,
    "wired_port_multicast": 0,
    "wired_port_broadcast": 0
  },
  "client_health_criteria": {
    "assoc_param_slow": 0,
    "assoc_unit_slow": "string",
    "auth_param_slow": 0,
    "auth_unit_slow": "string",
    "dhcp_param_slow": 0,
    "dhcp_unit_slow": "string",
    "roams_param_slow": 0,
    "roams_unit_slow": "string",
    "rssi_param": 0,
    "rssi_unit": "string",
    "snr_param": 0,
    "snr_unit": "string",
    "onboard_param": 0,
    "onboard_unit": "string"
  },
  "usage_capacity_criteria": {
    "channel_utilization": 0,
    "lnk_err": 0,
    "retries": 0,
    "pkt_loss": 0,
    "interference": 0,
    "noise": 0,
    "noise_unit": "string"
  }
}


response = requests.post(url, headers=headers, params=params)

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
