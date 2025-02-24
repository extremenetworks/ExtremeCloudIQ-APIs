import requests
         

access_token = '***'

url = f"https://api.extremecloudiq.com/subscriptions/webhook"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = [
  {
    "application": "example-app",
    "url": "https://webhook_endpoint-example-123",
    "secret": "erw3245cq3dasbjtyj",
    "message_type": "LOCATION_AP_CENTRIC"
  }
]


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
