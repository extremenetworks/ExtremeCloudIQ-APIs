import requests
import json

url = "https://api.extremecloudiq.com/subscriptions/webhook"

payload = json.dumps([
  {
    "application": "example-app",
    "url": "https://webhook_endpoint-example-123",
    "secret": "erw3245cq3dasbjtyj",
    "message_type": "LOCATION_AP_CENTRIC"
  }
])
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
