import requests
         

access_token = '***'

url = f"https://api.extremecloudiq.com/copilot/anomalies/update-device-action"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "anomalyDetails": [
    {
      "buildingId": 0,
      "locationId": 0,
      "anomalyId": "string",
      "anomalyType": "POE_STABILITY"
    }
  ],
  "actionType": "MUTE"
}
# async: false (disabled)

response = requests.put(url, headers=headers, params=params)

print("Status Code:", response.status_code)

content_type = response.headers.get('Content-Type')
lro_url = response.headers.get('Location')
if lro_url:
    print(lro_url)
elif content_type and 'application/json' in content_type:
    try:
        print("Response Body:", response.json())
    except ValueError:
        print("Response is not valid JSON")
else:
    print("Content-Type is not application/json")
    print(response.text)
