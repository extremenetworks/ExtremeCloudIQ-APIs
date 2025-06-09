import requests
         
baseUrl = 'api.extremecloudiq.com'
np_id = 'Network Policy ID'
pcgk_id = 'PCG Key Based Group ID'
access_token = '***'

url = f"https://{baseUrl}/pcgs/key-based/network-policy-{np_id}"
headers = {'Authorization': f'Bearer {access_token}'}
params = {'ids': f'{pcgk_id}'}



response = requests.delete(url, headers=headers, params=params)

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
