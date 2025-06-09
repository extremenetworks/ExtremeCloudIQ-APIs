import requests
         
baseUrl = 'api.extremecloudiq.com'
radio_usage_opt_id = 'Radio Usage Optimization Setting ID'
access_token = '***'

url = f"https://{baseUrl}/radio-profiles/radio-usage-opt/{radio_usage_opt_id}"
headers = {'Authorization': f'Bearer {access_token}'}
params = {}



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
