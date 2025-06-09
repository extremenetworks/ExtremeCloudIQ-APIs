import requests
         
baseUrl = 'api.extremecloudiq.com'
ssid_id = 'SSID ID'
access_token = '***'

url = f"https://{baseUrl}/ssids/{ssid_id}/mode/ppsk"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "key_management": "WPA_PSK",
  "encryption_method": "CCMP",
  "user_group_ids": [
    0
  ],
  "enable_max_clients_per_ppsk": True,
  "max_clients_per_ppsk": 15,
  "enable_mac_bind": True,
  "max_macs_per_ppsk": 5,
  "ppsk_server_id": 0
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
