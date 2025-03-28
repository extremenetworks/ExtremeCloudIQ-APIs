import requests
         

access_token = '***'

url = f"https://api.extremecloudiq.com/copilot/anomalies/exclude-vlans-csv"
headers = {'Authorization': f'Bearer {access_token}'}
params = {'action_type': 'ADD', 'dismiss': 'true'}



from requests_toolbelt.multipart.encoder import MultipartEncoder

files = {"csv_file": ('filename', open('Path-to-file/file.ext', 'rb'),'image/jpeg')}
payload = MultipartEncoder(fields=files)
headers["Content-Type"] = payload.content_type
response = requests.post(url, headers=headers, params=params, data=payload)

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
