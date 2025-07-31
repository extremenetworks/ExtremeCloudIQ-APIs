import requests
         
baseUrl = 'https://api.extremecloudiq.com'
neigh_analysis_id = 'Neighborhood Analysis Setting ID'
access_token = '***'

url = f"{baseUrl}/radio-profiles/neighborhood-analysis/{neigh_analysis_id}"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "enable_background_scan": True,
  "background_scan_interval": 1440,
  "enable_skip_scan_when_clients_connected": True,
  "enable_skip_scan_when_clients_in_power_save_mode": True,
  "enable_skip_scan_when_process_voice_traffic": True
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
