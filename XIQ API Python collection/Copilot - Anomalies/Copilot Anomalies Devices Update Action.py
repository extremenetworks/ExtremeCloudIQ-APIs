import requests
         
baseUrl = 'https://api.extremecloudiq.com'
access_token = '***'

url = f"{baseUrl}/copilot/anomalies/devices/update-action"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "anomaly_type": "POE_STABILITY",
  "action_type": "MUTE",
  "location_id": 0,
  "anomaly_id": "string"
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
