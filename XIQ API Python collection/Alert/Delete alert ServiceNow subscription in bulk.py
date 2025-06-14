import requests
         
baseUrl = 'api.extremecloudiq.com'
servicenow_id = 'ServiceNow subscription ID'
access_token = '***'

url = f"https://{baseUrl}/alert-subscriptions/servicenow/:delete"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}
body = {
  "ids": [
    servicenow_id
  ]
}
# async: false (disabled)

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
