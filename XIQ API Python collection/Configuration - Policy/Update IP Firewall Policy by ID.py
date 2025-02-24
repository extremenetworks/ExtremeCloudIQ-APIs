import requests
         
ip_firewall_policy_id = 'IP Firewall Policy ID'
access_token = '***'

url = f"https://api.extremecloudiq.com/ip-firewall-policies/{ip_firewall_policy_id}"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "name": "string",
  "description": "string",
  "rules": [
    {
      "action": "PERMIT",
      "service_id": 0,
      "source_ip_id": 0,
      "destination_ip_id": 0,
      "logging_type": "OFF"
    }
  ]
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
