import requests
         
baseUrl = 'api.extremecloudiq.com'
ssid_id = 'SSID ID'
access_token = '***'

url = f"https://{baseUrl}/ssids/{ssid_id}/mode/psk"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "key_management": "WPA_PSK",
  "encryption_method": "CCMP",
  "anti_logging_threshold": 0,
  "key_type": "ASCII",
  "key_value": "string",
  "sae_group": "ALL",
  "transition_mode": True
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
