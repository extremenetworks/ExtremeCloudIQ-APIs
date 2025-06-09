import requests
         
baseUrl = 'api.extremecloudiq.com'
radio_qos_id = 'Radio QoS Setting ID'
access_token = '***'

url = f"https://{baseUrl}/radio-profiles/wmm-qos/{radio_qos_id}"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "arbitration_interframe_space": 15,
  "min_contention_window": 15,
  "max_contention_window": 15,
  "transmission_opportunity_limit": 8192,
  "enable_no_ack": True
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
