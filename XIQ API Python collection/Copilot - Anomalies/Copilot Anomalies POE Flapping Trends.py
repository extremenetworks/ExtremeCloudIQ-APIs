import requests
         
baseUrl = 'api.extremecloudiq.com'
anomaly_id = 'Anomaly ID'
access_token = '***'

url = f"https://{baseUrl}/copilot/anomalies/poeflapping/trends"
headers = {'Authorization': f'Bearer {access_token}'}
params = {'anomalyId': f'{anomaly_id}'}



response = requests.get(url, headers=headers, params=params)

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
