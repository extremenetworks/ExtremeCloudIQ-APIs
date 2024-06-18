import requests

access_token = '***'

url = "https://api.extremecloudiq.com/account/viq/export?timeoutInSeconds=1800&excludeDeviceFirmware=false"

payload = {}
headers = {
  'Authorization': 'Bearer ' + access_token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
