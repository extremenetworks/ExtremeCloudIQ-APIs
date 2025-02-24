import requests
         
sensor_scan_id = 'Sensor Scan Setting ID'
access_token = '***'

url = f"https://api.extremecloudiq.com/radio-profiles/sensor-scan/{sensor_scan_id}"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "enable_scan_all_channels": True,
  "dwell_time": "string",
  "scan_channels": "string"
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
